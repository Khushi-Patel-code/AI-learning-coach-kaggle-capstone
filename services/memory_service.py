# services/memory_service.py

class MemoryService:
    """
    Very lightweight in-memory store.
    Used for:
    - Saving user preferences
    - Storing previous insights
    - Keeping key-value data across the workflow
    """

    def __init__(self):
        self.memory = {}

    def save(self, key: str, value):
        """Stores a key-value pair."""
        self.memory[key] = value

    def get(self, key: str, default=None):
        """Retrieves a stored value."""
        return self.memory.get(key, default)

    def clear(self):
        """Clears all memory."""
        self.memory = {}
