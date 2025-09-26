#!/usr/bin/python3

"""
Extending the Python Iter method
"""


class CountedIterator:
    """
    CountedIterator : An iterator that keeps track of the
            number of items iterated

    Attributes:
        data (list): The list of items to iterate
        counter (int): The count of items iterated
    """

    def __init__(self, data):
        """
        Initializes the CountedIterator with the given data.

        Args:
            data (list): The list of items to iterate over.
        """
        self.counter = 0
        self.data = data

    def get_count(self):
        """
        Returns the count of items iterated over.

        Returns:
            int: The count of items iterated over.
        """
        return self.counter

    def __next__(self):
        """
        __next__ Returns the next item in the data list
                and increments the counter

        Raises:
            StopIteration: Check if no more items to iterate

        Returns:
            Any: The next item in the data list
        """
        try:
            item = self.data[self.counter]
        except IndexError:
            raise StopIteration

        self.counter += 1
        return item
