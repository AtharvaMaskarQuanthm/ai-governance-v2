"""
Graph-based Retriever for GraphRAG

Expands retrieval results using the knowledge graph:
1. Find entities in initial results
2. Traverse graph to find related entities
3. Find additional sections mentioning related entities
4. Return expanded results for fusion
"""

import re
from pathlib import Path
from dataclasses import dataclass
from collections import defaultdict
from typing import Optional

import networkx as nx

# Add parent to path for imports
import sys
sys.path.insert(0, str(Path(__file__).parent.parent))

from indexing.graph_builder import KnowledgeGraphBuilder


@dataclass
class GraphExpansionResult:
    """Result from graph-based expansion."""
    section_id: str
    source_entities: list[str]  # Entities that led to this section
    hop_distance: int  # How many hops from original results
    relevance_score: float  # Based on entity overlap and hop distance


class GraphRetriever:
    """
    Expands retrieval using knowledge graph traversal.

    Strategy:
    1. Extract entities from initial retrieval results
    2. Find co-occurring and related entities (1-2 hops)
    3. Find sections that mention related entities
    4. Score based on entity overlap and hop distance
    """

    def __init__(self, graph_builder: KnowledgeGraphBuilder):
        self.graph = graph_builder.graph
        self.entity_to_sections = graph_builder.entity_to_sections
        self.section_to_entities = graph_builder.section_to_entities

    def _normalize_entity(self, entity_type: str, entity_value: str) -> str:
        """Normalize entity to match graph node ID format."""
        normalized = entity_value.lower().strip()
        normalized = re.sub(r'\s+', '_', normalized)
        normalized = re.sub(r'[^\w_]', '', normalized)
        return f"{entity_type}:{normalized}"

    def _extract_entities_from_query(self, query: str) -> list[str]:
        """
        Extract potential entity mentions from a query.

        Uses simple pattern matching for common security terms.
        """
        entities = []

        # Common role patterns
        role_patterns = [
            r'\b(CISO|CTO|CEO|IT\s+Manager|Security\s+Officer|Administrator)\b',
            r'\b(Information\s+Security\s+Team|Security\s+Team|IT\s+Team)\b',
        ]

        # Common control patterns
        control_patterns = [
            r'\b(MFA|multi-factor\s+authentication|two-factor|2FA)\b',
            r'\b(encryption|firewall|IDS|IPS|antivirus|anti-malware)\b',
            r'\b(access\s+control|password|authentication|authorization)\b',
            r'\b(backup|disaster\s+recovery|incident\s+response)\b',
            r'\b(vulnerability\s+assessment|penetration\s+testing|security\s+audit)\b',
        ]

        # Common asset patterns
        asset_patterns = [
            r'\b(server|database|network|application|system)\b',
            r'\b(endpoint|workstation|laptop|mobile\s+device)\b',
        ]

        # Common process patterns
        process_patterns = [
            r'\b(risk\s+assessment|incident\s+management|change\s+management)\b',
            r'\b(access\s+review|security\s+monitoring|log\s+review)\b',
        ]

        # Common framework patterns
        framework_patterns = [
            r'\b(ISO\s*27001|SEBI|CSCRF|CERT-IN|NIST|SOC\s*2)\b',
        ]

        # Extract matches
        patterns = [
            (role_patterns, "role"),
            (control_patterns, "control"),
            (asset_patterns, "asset"),
            (process_patterns, "process"),
            (framework_patterns, "framework"),
        ]

        for pattern_list, entity_type in patterns:
            for pattern in pattern_list:
                matches = re.findall(pattern, query, re.IGNORECASE)
                for match in matches:
                    if isinstance(match, tuple):
                        match = match[0]
                    entity_id = self._normalize_entity(entity_type, match)
                    if entity_id not in entities and self.graph.has_node(entity_id):
                        entities.append(entity_id)

        return entities

    def _get_related_entities(
        self,
        entity_ids: list[str],
        max_hops: int = 2
    ) -> dict[str, int]:
        """
        Find related entities within max_hops.

        Returns dict of entity_id → hop_distance
        """
        related = {}

        for entity_id in entity_ids:
            if not self.graph.has_node(entity_id):
                continue

            # BFS to find related entities
            visited = {entity_id: 0}
            queue = [(entity_id, 0)]

            while queue:
                current, distance = queue.pop(0)

                if distance >= max_hops:
                    continue

                # Get neighbors (both directions for undirected relationships)
                neighbors = set(self.graph.successors(current)) | set(self.graph.predecessors(current))

                for neighbor in neighbors:
                    neighbor_data = self.graph.nodes.get(neighbor, {})
                    neighbor_type = neighbor_data.get("node_type", "")

                    # Only follow entity-to-entity edges (CO_OCCURS)
                    # or entity relationships, not section/document nodes
                    if neighbor_type in ["section", "document"]:
                        continue

                    if neighbor not in visited:
                        visited[neighbor] = distance + 1
                        queue.append((neighbor, distance + 1))

                        # Track with minimum hop distance
                        if neighbor not in related or related[neighbor] > distance + 1:
                            related[neighbor] = distance + 1

        return related

    def _find_sections_for_entities(
        self,
        entity_ids: list[str],
        exclude_sections: set[str] = None
    ) -> dict[str, list[str]]:
        """
        Find sections that mention given entities.

        Returns dict of section_id → [entity_ids that appear in it]
        """
        exclude_sections = exclude_sections or set()
        section_entities = defaultdict(list)

        for entity_id in entity_ids:
            sections = self.entity_to_sections.get(entity_id, set())
            for section_id in sections:
                if section_id not in exclude_sections:
                    section_entities[section_id].append(entity_id)

        return dict(section_entities)

    def expand_results(
        self,
        initial_section_ids: list[str],
        query: str = "",
        max_hops: int = 2,
        max_expansion: int = 10
    ) -> list[GraphExpansionResult]:
        """
        Expand retrieval results using graph traversal.

        Args:
            initial_section_ids: Section IDs from initial retrieval
            query: Original query (for entity extraction)
            max_hops: Maximum graph traversal distance
            max_expansion: Maximum number of expanded results

        Returns:
            List of GraphExpansionResult for additional sections
        """
        # Collect entities from initial results
        seed_entities = set()
        for section_id in initial_section_ids:
            entities = self.section_to_entities.get(section_id, set())
            seed_entities.update(entities)

        # Also extract entities from query
        query_entities = self._extract_entities_from_query(query)
        seed_entities.update(query_entities)

        if not seed_entities:
            return []

        # Find related entities via graph traversal
        related_entities = self._get_related_entities(list(seed_entities), max_hops=max_hops)

        # Combine seed + related entities
        all_entities = list(seed_entities) + list(related_entities.keys())

        # Find sections mentioning these entities (excluding initial results)
        exclude = set(initial_section_ids)
        expanded_sections = self._find_sections_for_entities(all_entities, exclude)

        # Score and rank expanded sections
        results = []
        for section_id, matching_entities in expanded_sections.items():
            # Calculate relevance score
            # Higher score for: more entity matches, closer entities (fewer hops)
            direct_matches = sum(1 for e in matching_entities if e in seed_entities)
            indirect_matches = len(matching_entities) - direct_matches

            # Hop penalty for indirect matches
            hop_penalty = 0
            for entity in matching_entities:
                if entity in related_entities:
                    hop_penalty += related_entities[entity] * 0.1

            # Score: direct matches worth more than indirect
            score = (direct_matches * 1.0) + (indirect_matches * 0.5) - hop_penalty

            # Determine minimum hop distance
            min_hop = 0
            if direct_matches == 0:
                min_hop = min(
                    related_entities.get(e, max_hops)
                    for e in matching_entities
                    if e in related_entities
                ) if matching_entities else max_hops

            results.append(GraphExpansionResult(
                section_id=section_id,
                source_entities=matching_entities,
                hop_distance=min_hop,
                relevance_score=score
            ))

        # Sort by relevance score and limit
        results.sort(key=lambda x: x.relevance_score, reverse=True)
        return results[:max_expansion]

    def get_entity_context(self, entity_id: str) -> dict:
        """Get context about an entity from the graph."""
        if not self.graph.has_node(entity_id):
            return {}

        node_data = self.graph.nodes[entity_id]

        # Get co-occurring entities
        co_occurring = []
        for neighbor in self.graph.neighbors(entity_id):
            edge_data = self.graph.edges[entity_id, neighbor]
            if edge_data.get("edge_type") == "CO_OCCURS":
                co_occurring.append({
                    "entity": neighbor,
                    "weight": edge_data.get("weight", 1)
                })

        # Get sections mentioning this entity
        sections = list(self.entity_to_sections.get(entity_id, []))

        return {
            "entity_id": entity_id,
            "label": node_data.get("label", entity_id),
            "type": node_data.get("node_type", "unknown"),
            "co_occurring_entities": sorted(co_occurring, key=lambda x: x["weight"], reverse=True)[:10],
            "mentioned_in_sections": sections[:20]
        }


def load_graph_retriever(index_dir: str | Path) -> GraphRetriever:
    """Load a GraphRetriever from saved indexes."""
    graph_builder = KnowledgeGraphBuilder.load(index_dir)
    return GraphRetriever(graph_builder)


# CLI for testing
if __name__ == "__main__":
    project_root = Path(__file__).parent.parent.parent
    index_dir = project_root / "data" / "indexes"

    print("Loading graph retriever...")
    retriever = load_graph_retriever(index_dir)

    print(f"Graph has {retriever.graph.number_of_nodes()} nodes")

    # Test query
    test_query = "Organizations shall implement multi-factor authentication for privileged access"

    print(f"\nTest query: {test_query}")

    # Extract entities from query
    entities = retriever._extract_entities_from_query(test_query)
    print(f"\nExtracted entities from query: {entities}")

    # Simulate initial results
    initial_sections = ["CSP-6.3.2", "CSP-6.3.1"]

    # Expand
    expanded = retriever.expand_results(initial_sections, test_query, max_hops=2)

    print(f"\nExpanded results ({len(expanded)}):")
    for r in expanded[:5]:
        print(f"  {r.section_id} (score: {r.relevance_score:.2f}, hops: {r.hop_distance})")
        print(f"    via: {r.source_entities[:3]}")
