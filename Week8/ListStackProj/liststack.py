"""
File: liststack.py
Author: Man-Chi Leung
"""


class ListStack(object):
    """An list-based stack implementation."""

    # Constructor
    def __init__(self, sourceCollection=None):
        self.items = list()
        if sourceCollection:
            for item in sourceCollection:
                self.push(item)

    # Accessor methods
    def isEmpty(self):
        """Returns True if the stack is empty, or False otherwise."""
        return len(self.items) == 0

    def __len__(self):
        """Returns the number of items in the stack."""
        return len(self.items)

    def __str__(self):
        """Returns the string representation of the stack."""
        return "{" + ", ".join(map(str, self)) + "}"

    def __iter__(self):
        """Supports iteration over a view of the stack."""
        return iter(self.items)

    def __add__(self, other):
        """Returns a new stack containing the contents
        of self and other."""
        result = ListStack(self.items)
        for index in other:
            result.push(index)
        return result

    def __eq__(self, other):
        """Returns True if self equals other,
        or False otherwise."""
        return self.items == other.items

    def peek(self):
        """Returns the item at top of the stack.
        Precondition: the stack is not empty.
        Raises IndexError if stack is not empty."""
        if self.isEmpty():
            raise IndexError("Stack is empty")
        else:
            return self.items[len(self.items)-1]

    # Mutator methods
    def clear(self):
        """Makes self become empty."""
        return self.items.clear()

    def push(self, item):
        """Inserts item at top o the stack."""
        return self.items.append(item)

    def pop(self):
        """Removes and returns the item at top of the stack.
        Precondition: the stack is not empty.
        Raises IndexError if stack is not empty.
        Postcondition: the top item is removed from the stack."""
        if self.isEmpty():
            raise IndexError("Stack is empty")
        else:
            returnlist = list()
            count = 1
            for i in self.items:
                if not count == self.__len__():
                    returnlist.append(i)
                    count += 1
                elif count == self.__len__():
                    self.items = returnlist
                    return i

