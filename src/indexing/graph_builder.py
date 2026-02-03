"""
Knowledge Graph Builder for GraphRAG

Builds a NetworkX graph from parsed policy documents:
- Nodes: Entities (roles, controls, assets, processes), Documents, Sections
- Edges: Contains, CoOccurs, References, BelongsTo

Supports graph-based retrieval expansion.
"""

import json
import pickle
import re
from pathlib import Path
from dataclasses import dataclass, field
from collections import defaultdict
from typing import Optional

import networkx as nx

from .markdown_parser import parse_all_markdown_files, ParsedDocument, Section


@dataclass
class GraphStats:
    """Statistics about the knowledge graph."""
    total_nodes: int = 0
    total_edges: int = 0
    nodes_by_type: dict = field(default_factory=dict)
    edges_by_type: dict = field(default_factory=dict)


class KnowledgeGraphBuilder:
    """
    Builds a knowledge graph from policy documents.

    Node Types:
        - document: Policy documents
        - section: Document sections
        - role: Organizational roles (CISO, Information Security Team, etc.)
        - control: Security controls (Firewall, Encryption, MFA, etc.)
        - asset: Assets (Servers, Databases, etc.)
        - process: Business processes (Incident Management, etc.)
        - external: External parties (CERT-IN, SEBI, etc.)
        - framework: Regulatory frameworks (ISO27001, SEBI-CSCRF, etc.)

    Edge Types:
        - CONTAINS: document → section
        - HAS_ENTITY: section → entity
        - CO_OCCURS: entity ↔ entity (in same section)
        - REFERENCES: document → document
        - MAPS_TO: section → framework topic
    """

    def __init__(self):
        self.graph = nx.DiGraph()
        self.entity_to_sections = defaultdict(set)  # entity_id → {section_ids}
        self.section_to_entities = defaultdict(set)  # section_id → {entity_ids}

    def _normalize_entity_id(self, entity_type: str, entity_value: str) -> str:
        """Create a normalized node ID for an entity."""
        # Normalize: lowercase, replace spaces with underscores
        normalized = entity_value.lower().strip()
        normalized = re.sub(r'\s+', '_', normalized)
        normalized = re.sub(r'[^\w_]', '', normalized)
        return f"{entity_type}:{normalized}"

    def _add_entity_node(self, entity_type: str, entity_value: str) -> str:
        """Add an entity node to the graph."""
        node_id = self._normalize_entity_id(entity_type, entity_value)

        if not self.graph.has_node(node_id):
            self.graph.add_node(
                node_id,
                node_type=entity_type,
                label=entity_value,
                normalized=node_id
            )

        return node_id

    def _add_document_node(self, doc: ParsedDocument) -> str:
        """Add a document node to the graph."""
        node_id = f"doc:{doc.document_id}"

        self.graph.add_node(
            node_id,
            node_type="document",
            label=doc.title,
            document_id=doc.document_id,
            filepath=str(doc.filepath)
        )

        return node_id

    def _add_section_node(self, section: Section) -> str:
        """Add a section node to the graph."""
        node_id = f"section:{section.section_id}"

        self.graph.add_node(
            node_id,
            node_type="section",
            label=section.title,
            section_id=section.section_id,
            document_id=section.document_id,
            document_title=section.document_title,
            section_path=section.section_path,
            content_preview=section.content[:200] if section.content else ""
        )

        return node_id

    def add_document(self, doc: ParsedDocument):
        """Add a document and all its sections/entities to the graph."""
        doc_node = self._add_document_node(doc)

        # Add entities from frontmatter
        frontmatter_entities = doc.frontmatter.get("entities", {})
        for entity_type, entity_list in frontmatter_entities.items():
            if isinstance(entity_list, list):
                # Map frontmatter keys to our entity types
                type_mapping = {
                    "roles": "role",
                    "controls": "control",
                    "assets": "asset",
                    "processes": "process",
                    "external_parties": "external",
                    "frameworks": "framework"
                }
                mapped_type = type_mapping.get(entity_type, entity_type.rstrip('s'))

                for entity_value in entity_list:
                    entity_node = self._add_entity_node(mapped_type, entity_value)
                    # Document-level entity relationship
                    self.graph.add_edge(
                        doc_node, entity_node,
                        edge_type="MENTIONS",
                        source="frontmatter"
                    )

        # Add regulatory frameworks from frontmatter
        frameworks = doc.frontmatter.get("regulatory_frameworks", [])
        for fw in frameworks:
            if isinstance(fw, dict):
                fw_node = self._add_entity_node("framework", fw.get("name", fw.get("id", "")))
                self.graph.add_edge(doc_node, fw_node, edge_type="GOVERNED_BY")

        # Add document references
        references = doc.frontmatter.get("references", [])
        for ref in references:
            if isinstance(ref, dict):
                ref_doc_id = ref.get("document_id", "")
                if ref_doc_id:
                    ref_node = f"doc:{ref_doc_id}"
                    # Add placeholder node if doesn't exist
                    if not self.graph.has_node(ref_node):
                        self.graph.add_node(
                            ref_node,
                            node_type="document",
                            label=ref.get("title", ref_doc_id),
                            document_id=ref_doc_id
                        )
                    self.graph.add_edge(
                        doc_node, ref_node,
                        edge_type="REFERENCES",
                        relationship=ref.get("relationship", "related")
                    )

        # Add sections
        for section in doc.sections:
            section_node = self._add_section_node(section)

            # Document contains section
            self.graph.add_edge(doc_node, section_node, edge_type="CONTAINS")

            # Extract entities from section content
            section_entities = []

            # From parsed entities dict
            entity_types = {
                "roles": "role",
                "controls": "control",
                "assets": "asset",
                "processes": "process",
                "external": "external",
                "documents": "doc",
                "frameworks": "framework"
            }

            for entity_key, mapped_type in entity_types.items():
                for entity_value in section.entities.get(entity_key, []):
                    entity_node = self._add_entity_node(mapped_type, entity_value)
                    section_entities.append(entity_node)

                    # Section has entity
                    self.graph.add_edge(
                        section_node, entity_node,
                        edge_type="HAS_ENTITY"
                    )

                    # Track for retrieval
                    self.entity_to_sections[entity_node].add(section.section_id)
                    self.section_to_entities[section.section_id].add(entity_node)

            # Add co-occurrence edges between entities in same section
            for i, e1 in enumerate(section_entities):
                for e2 in section_entities[i+1:]:
                    if not self.graph.has_edge(e1, e2):
                        self.graph.add_edge(e1, e2, edge_type="CO_OCCURS", weight=1)
                    else:
                        # Increase weight for repeated co-occurrence
                        self.graph[e1][e2]["weight"] = self.graph[e1][e2].get("weight", 1) + 1

            # Add likely_maps_to relationships
            for topic in section.likely_maps_to:
                topic_node = self._add_entity_node("topic", topic)
                self.graph.add_edge(section_node, topic_node, edge_type="MAPS_TO")

    def build_from_documents(self, documents: list[ParsedDocument]):
        """Build the graph from a list of parsed documents."""
        for doc in documents:
            print(f"Adding to graph: {doc.title}")
            self.add_document(doc)

        print(f"\nGraph built: {self.graph.number_of_nodes()} nodes, {self.graph.number_of_edges()} edges")

    def get_stats(self) -> GraphStats:
        """Get statistics about the graph."""
        stats = GraphStats()
        stats.total_nodes = self.graph.number_of_nodes()
        stats.total_edges = self.graph.number_of_edges()

        # Count by type
        stats.nodes_by_type = defaultdict(int)
        for node, data in self.graph.nodes(data=True):
            node_type = data.get("node_type", "unknown")
            stats.nodes_by_type[node_type] += 1

        stats.edges_by_type = defaultdict(int)
        for u, v, data in self.graph.edges(data=True):
            edge_type = data.get("edge_type", "unknown")
            stats.edges_by_type[edge_type] += 1

        return stats

    def save(self, output_dir: str | Path):
        """Save the graph and lookup tables."""
        output_dir = Path(output_dir)
        output_dir.mkdir(parents=True, exist_ok=True)

        # Save graph as pickle
        graph_path = output_dir / "knowledge_graph.pkl"
        with open(graph_path, "wb") as f:
            pickle.dump(self.graph, f)

        # Save lookup tables
        lookups_path = output_dir / "graph_lookups.pkl"
        with open(lookups_path, "wb") as f:
            pickle.dump({
                "entity_to_sections": dict(self.entity_to_sections),
                "section_to_entities": dict(self.section_to_entities)
            }, f)

        # Save stats as JSON for easy inspection
        stats = self.get_stats()
        stats_path = output_dir / "graph_stats.json"
        with open(stats_path, "w") as f:
            json.dump({
                "total_nodes": stats.total_nodes,
                "total_edges": stats.total_edges,
                "nodes_by_type": dict(stats.nodes_by_type),
                "edges_by_type": dict(stats.edges_by_type)
            }, f, indent=2)

        print(f"Graph saved to {output_dir}")

    @classmethod
    def load(cls, input_dir: str | Path) -> "KnowledgeGraphBuilder":
        """Load a saved graph."""
        input_dir = Path(input_dir)

        builder = cls()

        # Load graph
        graph_path = input_dir / "knowledge_graph.pkl"
        with open(graph_path, "rb") as f:
            builder.graph = pickle.load(f)

        # Load lookups
        lookups_path = input_dir / "graph_lookups.pkl"
        with open(lookups_path, "rb") as f:
            lookups = pickle.load(f)
            builder.entity_to_sections = defaultdict(set, {
                k: set(v) for k, v in lookups["entity_to_sections"].items()
            })
            builder.section_to_entities = defaultdict(set, {
                k: set(v) for k, v in lookups["section_to_entities"].items()
            })

        return builder


def build_knowledge_graph(markdown_dir: str | Path, output_dir: str | Path) -> KnowledgeGraphBuilder:
    """
    Build and save a knowledge graph from markdown policy documents.

    Args:
        markdown_dir: Directory containing markdown policy files
        output_dir: Directory to save the graph

    Returns:
        The KnowledgeGraphBuilder instance
    """
    # Parse all documents
    documents = parse_all_markdown_files(markdown_dir)

    # Build graph
    builder = KnowledgeGraphBuilder()
    builder.build_from_documents(documents)

    # Save
    builder.save(output_dir)

    return builder


# CLI
if __name__ == "__main__":
    import sys

    project_root = Path(__file__).parent.parent.parent
    markdown_dir = project_root / "data" / "policies_md"
    output_dir = project_root / "data" / "indexes"

    print("Building knowledge graph...")
    builder = build_knowledge_graph(markdown_dir, output_dir)

    stats = builder.get_stats()
    print(f"\nGraph Statistics:")
    print(f"  Total nodes: {stats.total_nodes}")
    print(f"  Total edges: {stats.total_edges}")
    print(f"\n  Nodes by type:")
    for node_type, count in sorted(stats.nodes_by_type.items()):
        print(f"    {node_type}: {count}")
    print(f"\n  Edges by type:")
    for edge_type, count in sorted(stats.edges_by_type.items()):
        print(f"    {edge_type}: {count}")
