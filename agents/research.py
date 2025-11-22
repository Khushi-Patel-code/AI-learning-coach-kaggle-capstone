"""
agents/research.py
Research agent for the orchestrator.

Right now this uses a mock "search" and returns structured results.
Later you can integrate:
 - Google Custom Search JSON API
 - Kaggle datasets
 - academic APIs
 - ADK tools
"""

import logging
import time
from typing import Dict, Any

logger = logging.getLogger("researcher")
logger.setLevel(logging.DEBUG)


class Researcher:
    """Research agent that fetches information for a given query."""

    def __init__(self, latency: float = 0.6):
        self.latency = latency

    def research(self, query: str) -> Dict[str, Any]:
        logger.debug("Researcher: researching query: %s", query)

        # simulated delay (replace with real search later)
        time.sleep(self.latency)

        # simple structured result
        result = {
            "query": query,
            "top_results": [
                f"Top insight for '{query}' (mock source)",
                f"Additional supporting detail for '{query}'"
            ],
            "extra": {
                "confidence": 0.85
            }
        }

        logger.debug("Researcher: completed research for query: %s", query)
        return result
