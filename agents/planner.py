"""
agents/planner.py
Enhanced Planner that uses memory context to adapt plans.

The Planner outputs a list of steps.
Each step is a dict with keys:
  - step_id (str)
  - type ("research" or "summarize")
  - query (for research)
  - child_steps (for summarize)
"""

import logging
import uuid
from typing import List, Dict, Any, Optional

logger = logging.getLogger("planner")
logger.setLevel(logging.DEBUG)


class Planner:
    """Generate a structured plan for the orchestrator, with memory-aware context."""

    def __init__(self):
        pass

    def _new_step_id(self) -> str:
        return "s_" + uuid.uuid4().hex[:6]

    # -------------------------------------------------------------
    # NEW: Memory-aware create_plan()
    # -------------------------------------------------------------
    def create_plan(self, mission: str, previous_plan: Optional[List] = None) -> List[Dict[str, Any]]:
        """
        Creates a 3-step plan but improves it when previous memory exists.

        Behaviors:
        - If no previous plan: standard 3-step research → deep → summary
        - If previous plan exists: planner adds "build on previous insights"
        - If previous research exists: planner narrows or evolves queries
        """
        logger.debug("Planner: creating plan for mission: %s", mission)

        # =========================================================
        # CASE 1: No previous plan — Standard 3-step plan
        # =========================================================
        if not previous_plan:
            logger.debug("Planner: no previous plan found, generating standard plan.")

            s1 = {
                "step_id": self._new_step_id(),
                "type": "research",
                "query": f"General overview and background for: {mission}",
            }
            s2 = {
                "step_id": self._new_step_id(),
                "type": "research",
                "query": f"Important methods, techniques, and challenges related to: {mission}",
            }
            s3 = {
                "step_id": self._new_step_id(),
                "type": "summarize",
                "child_steps": [s1["step_id"], s2["step_id"]],
            }

            plan = [s1, s2, s3]
            logger.debug("Planner: standard plan created with %d steps", len(plan))
            return plan

        # =========================================================
        # CASE 2: Previous plan exists — Build adaptive/iterative plan
        # =========================================================
        logger.debug("Planner: previous plan found, generating adaptive enhanced plan.")

        # Extract previous step queries for adaptation
        last_queries = [
            step.get("query", "")
            for step in previous_plan
            if step["type"] == "research"
        ]

        # Adaptive new research queries
        refined_query = (
            f"Refined insights based on past learning progress for mission: {mission}. "
            f"Build upon previous queries: {', '.join(last_queries)}"
        )

        deep_dive_query = (
            f"Advanced strategies and actionable techniques to improve results for: {mission}. "
            f"Focus on areas previously identified as important."
        )

        # New steps
        s1 = {
            "step_id": self._new_step_id(),
            "type": "research",
            "query": refined_query,
        }
        s2 = {
            "step_id": self._new_step_id(),
            "type": "research",
            "query": deep_dive_query,
        }
        s3 = {
            "step_id": self._new_step_id(),
            "type": "summarize",
            "child_steps": [s1["step_id"], s2["step_id"]],
        }

        plan = [s1, s2, s3]
        logger.debug("Planner: adaptive plan created with %d steps", len(plan))

        return plan
