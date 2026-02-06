#!/usr/bin/env python3
"""
VerboseList class that extends Python's built-in list
and prints notifications on modifications.
"""

class VerboseList(list):
    def append(self, item):
        """Append item and print notification."""
        super().append(item)
        print(f"Added [{item}] to the list.")

    def extend(self, iterable):
        """Extend list and print notification with item count."""
        count = len(iterable)
        super().extend(iterable)
        print(f"Extended the list with [{count}] items.")

    def remove(self, item):
        """Remove item and print notification."""
        print(f"Removed [{item}] from the list.")
        super().remove(item)

    def pop(self, index=-1):
        """Pop item at index and print notification."""
        item = self[index]  # Get the item before removal
        print(f"Popped [{item}] from the list.")
        return super().pop(index)
