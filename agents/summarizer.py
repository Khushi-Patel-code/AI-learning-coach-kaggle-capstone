from tools.summarizer_tool import SummarizerTool

class Summarizer:
    def __init__(self):
        self.tool = SummarizerTool()

    def summarize_research(self, research_results):
        """
        Called by Orchestrator.
        Combine all research results & summarize them.
        """
        collected_text = ""

        for step in research_results:
            if isinstance(step, dict) and "top_results" in step:
                collected_text += " ".join(step["top_results"]) + " "

        return self.tool.summarize(collected_text)

    # Optional: keep old method for compatibility
    def summarize(self, research_results):
        return self.summarize_research(research_results)
