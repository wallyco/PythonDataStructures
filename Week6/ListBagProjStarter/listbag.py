"""
File: listbag.py
Author: Man-Chi Leung
"""

class ListBag(object):
    """A list-based bag implementation."""

    # Constructor
    def __init__(self, sourceCollection=None):
        """Sets the initial state of self, which includes the
        contents of sourceCollection, if it's present."""
        self.collection = list()
        if sourceCollection:
            for item in sourceCollection:
                self.add(item)

    # Accessor methods
    def isEmpty(self):
        """Returns True if len(self) == 0, or False otherwise."""
        return len(self.collection) == 0

    def __len__(self):
        """Returns the number of items in self."""
        return len(self.collection)

    def __str__(self):
        """Returns the string representation of self."""
        return "{" + ", ".join(map(str,self)) + "}"

    def __iter__(self):
        """Supports iteration over a view of self."""
        return iter(self.collection)

    def __add__(self, other):
        """Returns a new bag containing the contents
        of self and other."""
        result = ListBag(self.collection)
        for item in other:
            result.collection.append(item)
        return result

    def __eq__(self, other):
        """Returns True if self equals other,
        or False otherwise."""
        if self is other:
            return True
        for item in self:
            if self.count(item) != other.count(item):
                return False
        return True

    def count(self, item):
        """Returns the number of instances of item in self."""
        count = 0
        for index in self:
            if index == item:
                count += 1
        return count

    # Mutator methods
    def clear(self):
        """Makes self become empty."""
        self.collection.clear()

    def add(self, item):
        """Adds item to self."""
        self.collection.append(item)

    def remove(self, item):
        """Precondition: item is in self.
        Raises: KeyError if item in not in self.
        Postcondition: item is removed from self."""
        if not item in self:
            raise KeyError(str(item) + " is not in this bag")

        self.collection.remove(item)
