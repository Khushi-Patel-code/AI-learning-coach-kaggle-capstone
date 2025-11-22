"""
agents/coach.py
Produces the final user-facing result.

This agent converts:
 - plan
 - summary
 - mission

into a final structured output.

In the real version, you may:
 - generate a weekly study plan
 - produce a formatted report
 - generate tips, pitfalls, metrics, checklists
 - include memory personalization
"""

import logging
from typing import List, Dict, Any

logger = logging.getLogger("coach")
logger.setLevel(logging.DEBUG)


class Coach:
    """Transform the orchestrator output into final guidance for the user."""

    def __init__(self):
        pass

    def create_output(
        self, mission: str, plan: List[Dict[str, Any]], summary: str
    ) -> Dict[str, Any]:

        logger.debug("Coach: creating final output for mission='%s'", mission)

        output = {
            "mission": mission,
            "summary": summary,
            "steps_explained": [
                f"Step {i+1}: {step['type']} - {step.get('query', step.get('child_steps'))}"
                for i, step in enumerate(plan)
            ],
            "action_recommendation": (
                f"For this mission ('{mission}'), follow the above plan. "
                f"Focus on: {summary[:180]}"
            ),
        }

        return output
