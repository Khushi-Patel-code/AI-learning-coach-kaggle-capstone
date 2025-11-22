# tools/plan_formatter.py

class PlanFormatter:
    """
    Formats a structured plan (list of tasks) into a clean text output.
    """

    def format_plan(self, tasks: list[str]) -> str:
        if not tasks:
            return "No tasks generated."

        output = ["Your personalized learning plan:\n"]
        for i, t in enumerate(tasks, start=1):
            output.append(f"{i}. {t}")

        return "\n".join(output)
