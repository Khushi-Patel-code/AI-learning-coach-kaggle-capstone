"""
agents/summarizer.py
Summarizes multiple research results into a compressed explanation.

Later:
 - Replace with an LLM summarization step using ADK
 - Add compression tools
 - Add academic citation tools
"""

import logging
from typing import List, Dict, Any

logger = logging.getLogger("summarizer")
logger.setLevel(logging.DEBUG)


class Summarizer:
    """Combine research pieces into an interpretable summary."""

    def __init__(self):
        pass

    def summarize(self, pieces: List[Dict[str, Any]]) -> str:
        logger.debug("Summarizer: summarizing %d pieces", len(pieces))

        extracted = []
        for p in pieces:
            first = ""
            if "top_results" in p and len(p["top_results"]) > 0:
                first = p["top_results"][0]
            else:
                first = "(missing research data)"
            extracted.append(first)

        summary = " | ".join(extracted)
        final = f"Summary: {summary}"

        logger.debug("Summarizer: summary produced")
        return final
