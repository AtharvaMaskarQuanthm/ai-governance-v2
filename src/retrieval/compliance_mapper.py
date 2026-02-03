"""
Compliance Mapper

Takes a regulatory requirement and finds how it's addressed in internal policies.
Provides:
- Relevant policy sections
- Coverage assessment (FULL / PARTIAL / NOT_COVERED)
- Gap analysis
- Recommendations
"""

import json
from dataclasses import dataclass
from typing import Optional
from openai import OpenAI

from .hybrid_retriever import HybridRetriever, RetrievalResult


@dataclass
class PolicyMapping:
    """A mapping from requirement to policy section."""
    section_id: str
    section_title: str
    document_title: str
    relevance: str  # How this section addresses the requirement
    excerpt: str  # Relevant excerpt from the section
    coverage_strength: str  # STRONG / MODERATE / WEAK


@dataclass
class ComplianceResult:
    """Full compliance mapping result."""
    requirement: str
    coverage: str  # FULL / PARTIAL / NOT_COVERED
    confidence: float  # 0-1 confidence in the assessment
    mappings: list[PolicyMapping]
    gaps: list[dict]  # {"aspect": ..., "gap_description": ...}
    recommendations: list[str]
    raw_results: list[RetrievalResult]  # Original retrieval results


ANALYSIS_SYSTEM_PROMPT = """You are a compliance auditor analyzing whether internal policies adequately address regulatory requirements.

You will be given:
1. A regulatory requirement
2. Retrieved policy sections that may address it

Your job is to analyze coverage and output a JSON response.

## Output Format (JSON only, no markdown):
{
  "coverage": "FULL" | "PARTIAL" | "NOT_COVERED",
  "confidence": 0.0-1.0,
  "mappings": [
    {
      "section_id": "CSP-6.3.2",
      "section_title": "Logical Access Security",
      "document_title": "Cyber Security Policy",
      "relevance": "How this section addresses the requirement",
      "excerpt": "Direct quote from the policy (max 200 chars)",
      "coverage_strength": "STRONG" | "MODERATE" | "WEAK"
    }
  ],
  "gaps": [
    {
      "aspect": "What aspect of the requirement",
      "gap_description": "What's missing or insufficient"
    }
  ],
  "recommendations": [
    "Specific actionable recommendation to address gaps"
  ]
}

## Guidelines:
- FULL: All aspects of the requirement are clearly addressed
- PARTIAL: Some aspects addressed, others missing or unclear
- NOT_COVERED: No relevant policy content found
- Be specific about what IS covered and what IS NOT
- Quote directly from policies when possible
- Recommendations should be actionable"""


class ComplianceMapper:
    """
    Maps regulatory requirements to internal policy sections.
    """

    def __init__(
        self,
        retriever: HybridRetriever,
        openai_client: Optional[OpenAI] = None,
        analysis_model: str = "gpt-4o"
    ):
        self.retriever = retriever
        self.client = openai_client or OpenAI()
        self.analysis_model = analysis_model

    def _format_retrieved_sections(self, results: list[RetrievalResult]) -> str:
        """Format retrieved sections for the analysis prompt."""
        sections = []
        for i, r in enumerate(results, 1):
            sections.append(f"""
--- Section {i} ---
ID: {r.section_id}
Title: {r.section_title}
Document: {r.document_title}
Path: {r.section_path}
Retrieval Score: {r.score:.4f}
Sources: {', '.join(r.sources)}

Content:
{r.content}
""")
        return "\n".join(sections)

    def _analyze_coverage(
        self,
        requirement: str,
        results: list[RetrievalResult]
    ) -> dict:
        """Use LLM to analyze coverage."""
        sections_text = self._format_retrieved_sections(results)

        user_prompt = f"""## Regulatory Requirement:
{requirement}

## Retrieved Policy Sections:
{sections_text}

Analyze how well these policy sections address the regulatory requirement.
Output ONLY valid JSON matching the specified format."""

        response = self.client.chat.completions.create(
            model=self.analysis_model,
            messages=[
                {"role": "system", "content": ANALYSIS_SYSTEM_PROMPT},
                {"role": "user", "content": user_prompt}
            ],
            max_tokens=2000,
            temperature=0.1,
            response_format={"type": "json_object"}
        )

        return json.loads(response.choices[0].message.content)

    def map_requirement(
        self,
        requirement: str,
        top_k: int = 10,
        use_hyde: bool = True
    ) -> ComplianceResult:
        """
        Map a regulatory requirement to internal policies.

        Args:
            requirement: The regulatory requirement text
            top_k: Number of policy sections to retrieve
            use_hyde: Whether to use HyDE for better retrieval

        Returns:
            ComplianceResult with full analysis
        """
        # Retrieve relevant sections
        results = self.retriever.search(
            requirement,
            top_k=top_k,
            use_hyde=use_hyde
        )

        if not results:
            return ComplianceResult(
                requirement=requirement,
                coverage="NOT_COVERED",
                confidence=0.9,
                mappings=[],
                gaps=[{"aspect": "Entire requirement", "gap_description": "No relevant policy sections found"}],
                recommendations=["Create policy content to address this requirement"],
                raw_results=[]
            )

        # Analyze coverage with LLM
        analysis = self._analyze_coverage(requirement, results)

        # Build mappings
        mappings = []
        for m in analysis.get("mappings", []):
            mappings.append(PolicyMapping(
                section_id=m.get("section_id", ""),
                section_title=m.get("section_title", ""),
                document_title=m.get("document_title", ""),
                relevance=m.get("relevance", ""),
                excerpt=m.get("excerpt", ""),
                coverage_strength=m.get("coverage_strength", "MODERATE")
            ))

        return ComplianceResult(
            requirement=requirement,
            coverage=analysis.get("coverage", "PARTIAL"),
            confidence=analysis.get("confidence", 0.5),
            mappings=mappings,
            gaps=analysis.get("gaps", []),
            recommendations=analysis.get("recommendations", []),
            raw_results=results
        )

    def map_multiple_requirements(
        self,
        requirements: list[str],
        top_k: int = 10,
        use_hyde: bool = True
    ) -> list[ComplianceResult]:
        """Map multiple requirements."""
        results = []
        for i, req in enumerate(requirements, 1):
            print(f"Processing requirement {i}/{len(requirements)}...")
            result = self.map_requirement(req, top_k=top_k, use_hyde=use_hyde)
            results.append(result)
        return results


def format_compliance_result(result: ComplianceResult, verbose: bool = False) -> str:
    """Format a compliance result for display."""
    lines = []

    # Header
    coverage_indicator = {
        "FULL": "[FULL]",
        "PARTIAL": "[PARTIAL]",
        "NOT_COVERED": "[NOT COVERED]"
    }
    indicator = coverage_indicator.get(result.coverage, "[?]")

    lines.append(f"\n{'='*70}")
    lines.append(f"REQUIREMENT:")
    lines.append(f"{result.requirement}")
    lines.append(f"{'='*70}")
    lines.append(f"\n{indicator} Coverage: {result.coverage} (confidence: {result.confidence:.0%})")

    # Mappings
    if result.mappings:
        lines.append(f"\nPOLICY MAPPINGS ({len(result.mappings)} sections):")
        for m in result.mappings:
            strength_indicator = {"STRONG": "[***]", "MODERATE": "[** ]", "WEAK": "[*  ]"}.get(m.coverage_strength, "[   ]")
            lines.append(f"\n  [{m.section_id}] {m.section_title}")
            lines.append(f"  Document: {m.document_title}")
            lines.append(f"  Strength: {strength_indicator} {m.coverage_strength}")
            lines.append(f"  Relevance: {m.relevance}")
            if m.excerpt:
                lines.append(f"  Excerpt: \"{m.excerpt[:150]}...\"")

    # Gaps
    if result.gaps:
        lines.append(f"\nGAPS IDENTIFIED ({len(result.gaps)}):")
        for g in result.gaps:
            lines.append(f"  - {g.get('aspect', 'Unknown')}")
            lines.append(f"    > {g.get('gap_description', '')}")

    # Recommendations
    if result.recommendations:
        lines.append(f"\nRECOMMENDATIONS:")
        for r in result.recommendations:
            lines.append(f"  - {r}")

    # Verbose: show raw retrieval results
    if verbose and result.raw_results:
        lines.append(f"\nRAW RETRIEVAL RESULTS:")
        for r in result.raw_results[:5]:
            lines.append(f"  [{r.section_id}] {r.section_title} (score: {r.score:.4f}, via: {','.join(r.sources)})")

    lines.append("")
    return "\n".join(lines)
