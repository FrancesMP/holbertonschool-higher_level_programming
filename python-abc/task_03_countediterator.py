#!/usr/bin/env python3
"""
CountedIterator: keep track of how many items have been iterated.
"""


class CountedIterator:
    """Iterator wrapper that counts how many items you’ve gone through."""

    def __init__(self, iterable):
        """
        Create a CountedIterator.

        Args:
            iterable (iterable): Any iterable (list, tuple, generator, etc.)
        """
        self.iterator = iter(iterable)
        self.count = 0

    def __iter__(self):
        """Return self so it works in for-loops."""
        return self

    def __next__(self):
        """
        Fetch the next item and update the count.
        Raises StopIteration when the underlying iterator is done.
        """
        item = next(self.iterator)  # may raise StopIteration naturally
        self.count += 1
        return item

    def get_count(self):
        """Return how many items have been iterated so far."""
        return self.count
