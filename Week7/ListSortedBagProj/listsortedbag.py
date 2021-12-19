"""
File: listbag.py
Author: Man-Chi Leung
"""

from listbag import ListBag


class ListSortedBag(ListBag):
    """An list-based bag implementation."""

    # Constructor
    def __init__(self, sourceCollection=None):
        """Sets the initial state of self, which includes the
        contents of sourceCollection, if it's present."""
        ListBag.__init__(self, sourceCollection)

    def __contains__(self, item, p=True):
        """Returns True if item is in self, or False otherwise.
        Use binary search"""
        left = 0
        right = len(self.items) - 1
        visited = []
        while left <= right:
            midPoint = (left + right) // 2
            visited.append(self.items[midPoint])
            if self.items[midPoint] == item:
                if p:
                    print("Items Visited: " + str(visited))
                return True
            elif self.items[midPoint] > item:
                right = midPoint - 1
            else:
                left = midPoint + 1
        if p:
            print("Items Visited: " + str(visited))
        return False

    def __add__(self, other):
        """Returns a new bag containing the contents
        of self and other."""
        result = ListSortedBag(self.items)
        for item in other:
            result.add(item)
        return result

    def add(self, item):
        """Adds item to self."""
        if not self.__contains__(item, False):
            if self.__len__() == 0:
                self.items.append(item)
                print("Item added: %s To the front" % item)
            elif item > self.items[self.__len__() - 1]:
                print("Item added: %s To the back" % item)
                self.items.append(item)
            elif item < self.items[0]:
                print("Item added: %s To the front" % item)
                self.items.insert(0, item)
            else:
                head = 0
                visited = []
                while item > self.items[head]:
                    visited.append(self.items[head])
                    if item > self.items[head]:
                        if item < self.items[head + 1]:
                            print("Item added: %s Items visited: " % item + str(visited))
                            self.items.insert(head + 1, item)
                    head += 1

    def remove(self, item):
        """Removes item from self."""
        if self.__contains__(item):
            self.items.remove(item)
        else:
            raise KeyError(str(item) + " is not in this bag")
