"""
File: listset.py
Author: Man-Chi Leung
"""


class ListSet(object):
    """A list-based set implementation."""

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
        return "{" + ", ".join(map(str, self)) + "}"

    def __iter__(self):
        """Supports iteration over a view of self."""
        return iter(self.collection)

    def __add__(self, other):
        """Returns a new set containing the contents
        of self and other."""

        result = ListSet(self.collection)
        for item in other:
            result.add(item)
        return result

    def __eq__(self, other):
        """Returns True if self equals other,
        or False otherwise."""
        self.collection.sort()
        other.collection.sort()
        return self.collection == other.collection

    # Mutator methods
    def clear(self):
        """Makes self become empty."""
        self.collection.clear()

    def add(self, item):
        """Adds item to self."""
        isunique = True
        for index in self:
            if index == item:
                isunique = False
        if isunique:
            self.collection.append(item)

    def remove(self, item):
        """Precondition: item is in self.
        Raises: KeyError if item in not in self.
        Postcondition: item is removed from self."""
        if item not in self:
            raise KeyError(str(item) + " is not in this bag")

        self.collection.remove(item)
