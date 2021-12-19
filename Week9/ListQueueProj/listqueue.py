"""
File: listqueue.py
Author: Man-Chi Leung
"""


class ListQueue(object):
    """An list-based stack implementation."""

    # Constructor
    def __init__(self, sourceCollection=None):
        """Sets the initial state of self, which includes the
        contents of sourceCollection, if it's present."""
        self.items = list()
        if sourceCollection:
            for item in sourceCollection:
                self.add(item)

    # Accessor methods
    def isEmpty(self):
        """Returns True if the queue is empty, or False otherwise."""
        return len(self.items) == 0

    def __len__(self):
        """Returns the number of items in the queue."""
        return len(self.items)

    def __str__(self):
        """Returns the string representation of the queue."""
        return "{" + ", ".join(map(str, self)) + "}"

    def __iter__(self):
        """Supports iteration over a view of the queue."""
        return iter(self.items)

    def __add__(self, other):
        """Returns a new queue containing the contents
        of self and other."""
        result = ListQueue(self.items)
        for index in other:
            result.add(index)
        return result

    def __eq__(self, other):
        """Returns True if self equals other,
        or False otherwise."""
        return self.items == other.items

    def peek(self):
        """Returns the item at the front of the queue.
        Precondition: the queue is not empty.
        Raises IndexError if queue is not empty."""
        if self.isEmpty():
            raise IndexError("Stack is empty")
        else:
            return self.items[0]

    # Mutator methods
    def clear(self):
        """Makes self become empty."""
        return self.items.clear()

    def add(self, item):
        """Inserts item at rear of the queue."""
        return self.items.append(item)

    def pop(self):
        """Removes and returns the item at the front of the queue.
        Precondition: the queue is not empty.
        Raises IndexError if queue is not empty.
        Postcondition: the front item is removed from the queue."""
        if self.isEmpty():
            raise IndexError("Stack is empty")
        else:
            returnlist = list()
            count = 0
            returnval = 0
            for i in self.items:
                if count == 0:
                    returnval = i
                    count += 1
                else:
                    returnlist.append(i)
            self.items = returnlist
            return returnval
