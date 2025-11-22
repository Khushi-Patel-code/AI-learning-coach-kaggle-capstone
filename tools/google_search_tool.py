# tools/google_search_tool.py

class GoogleSearchTool:
    """
    A lightweight simulated search tool.
    Replace with real API calls later if needed.
    """

    def search(self, query: str) -> str:
        # Stubbed response — you may later integrate Serper, Tavily, etc.
        results = [
            f"Result 1 for '{query}': Basic explanation found.",
            f"Result 2 for '{query}': Example-driven tutorial.",
            f"Result 3 for '{query}': Best practices and tips."
        ]
        return "\n".join(results)
