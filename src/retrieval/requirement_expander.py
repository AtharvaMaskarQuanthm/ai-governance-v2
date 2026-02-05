"""
Requirement Expander

Pre-retrieval LLM expansion that decomposes a regulatory requirement into
sub-requirements, implicit aspects, search terms, and framework references
to improve multi-pass search recall.
"""

import json
import logging
from dataclasses import dataclass, field
from typing import Optional
from openai import OpenAI

logger = logging.getLogger(__name__)

EXPANSION_SYSTEM_PROMPT = """You are a regulatory compliance expert specializing in Indian financial sector regulations (SEBI CSCRF, CERT-IN directives), ISO 27001, and NIST Cybersecurity Framework.

Given a regulatory requirement, decompose it into structured components for compliance mapping.

Output a JSON object with these fields:

1. "sub_requirements": Break the requirement into 2-5 atomic obligations. Each should be a single, testable compliance statement. Do NOT restate the original requirement.

2. "implicit_aspects": List 2-4 compliance aspects that are implied but not explicitly stated (e.g., documentation, periodic review, incident response, training).

3. "search_terms": Provide 5-15 alternative phrasings, synonyms, acronyms, and related terms that internal policies might use instead of the regulatory language. Include both formal and informal terms.

4. "related_frameworks": List 2-6 specific framework references (e.g., "ISO 27001 A.9.4.2", "NIST CSF PR.AC-7", "SEBI CSCRF 4.3") that address similar controls.

Be precise and actionable. Focus on terms that would appear in internal security policies of Indian financial organizations."""


@dataclass
class ExpandedRequirement:
    """A regulatory requirement decomposed into searchable components."""
    original: str
    sub_requirements: list[str] = field(default_factory=list)
    implicit_aspects: list[str] = field(default_factory=list)
    search_terms: list[str] = field(default_factory=list)
    related_frameworks: list[str] = field(default_factory=list)

    def search_terms_query(self) -> str:
        """Join search terms into a BM25 query string."""
        return " ".join(self.search_terms)

    def context_for_analysis(self) -> str:
        """Format expansion for inclusion in the analysis LLM prompt."""
        parts = []
        if self.sub_requirements:
            parts.append("Sub-requirements:")
            for i, sr in enumerate(self.sub_requirements, 1):
                parts.append(f"  {i}. {sr}")
        if self.implicit_aspects:
            parts.append("Implicit compliance aspects:")
            for aspect in self.implicit_aspects:
                parts.append(f"  - {aspect}")
        if self.related_frameworks:
            parts.append("Related frameworks:")
            for fw in self.related_frameworks:
                parts.append(f"  - {fw}")
        return "\n".join(parts)


class RequirementExpander:
    """Expands a regulatory requirement into sub-requirements, search terms, and framework references."""

    def __init__(self, openai_client: Optional[OpenAI] = None, model: str = "gpt-4o-mini"):
        self.client = openai_client or OpenAI()
        self.model = model

    def expand(self, requirement: str) -> ExpandedRequirement:
        """
        Expand a regulatory requirement into structured components.

        Args:
            requirement: The regulatory requirement text

        Returns:
            ExpandedRequirement with decomposed components
        """
        response = self.client.chat.completions.create(
            model=self.model,
            messages=[
                {"role": "system", "content": EXPANSION_SYSTEM_PROMPT},
                {"role": "user", "content": requirement}
            ],
            response_format={"type": "json_object"},
            temperature=0.2,
            max_tokens=800
        )

        raw = json.loads(response.choices[0].message.content)

        return ExpandedRequirement(
            original=requirement,
            sub_requirements=raw.get("sub_requirements", []),
            implicit_aspects=raw.get("implicit_aspects", []),
            search_terms=raw.get("search_terms", []),
            related_frameworks=raw.get("related_frameworks", []),
        )
