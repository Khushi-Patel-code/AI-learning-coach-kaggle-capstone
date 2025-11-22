# tools/summarizer_tool.py

class SummarizerTool:
    """
    Simple text summarizer for condensing content.
    """

    def summarize(self, text: str, max_sentences: int = 3) -> str:
        if not text:
            return "No content to summarize."

        sentences = text.split(". ")
        summary = sentences[:max_sentences]

        return ". ".join(summary).strip() + "."
