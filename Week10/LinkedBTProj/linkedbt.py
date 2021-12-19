"""
File: linkedbt.py
"""

from abstractcollection import AbstractCollection
from btnode import BTNode


class LinkedBT(AbstractCollection):
    """An link-based binary search tree implementation."""

    def __init__(self, sourceCollection=None):
        """Sets the initial state of self, which includes the
        contents of sourceCollection, if it's present."""
        self.root = None
        AbstractCollection.__init__(self, sourceCollection)

    # Accessor methods
    def __str__(self):
        """Returns a string representation with the tree rotated
        90 degrees counterclockwise."""

        def recurse(node, level):
            s = ""
            if node != None:
                s += recurse(node.right, level + 1)
                s += "| " * level
                s += str(node.data) + "\n"
                s += recurse(node.left, level + 1)
            return s

        return recurse(self.root, 0)

    def find(self, item):
        """If item matches an item in self, returns the
        node that matches item, or None otherwise."""

        def recurse(node, item):
            if node != None:
                if node.data == item:
                    return node
                returned_node = recurse(node.left, item)
                if returned_node != None:
                    return returned_node
                else:
                    return recurse(node.right, item)
            else:
                return None

        return recurse(self.root, item)

    def __iter__(self):
        returnlist = []
        def recurse(node):
            if node is not None:
                returnlist.append(node.data)
                recurse(node.left)
                recurse(node.right)
            else:
                return None
        recurse(self.root)
        for i in returnlist:
            yield i

    # Mutator methods
    def clear(self):
        """Makes self become empty."""
        self.root = BTNode(None)
        self.size = 0

    def add(self, item, parent=None, side='left'):
        """Adds item to the tree."""
        node = BTNode(item)
        if self.isEmpty():
            self.root = node
            self.size += 1
            print(f"{item} added as root")
        elif parent is not None:
            if self.find(parent) is None:
                print("Parent node: %s is not found in the tree" % parent)
            else:
                parentnode = self.find(parent)
                if side == 'left' and parentnode.left is None:
                    parentnode.left = node
                    self.size += 1
                    print(f"New node added. Parent: {parentnode.data}, Left Child: {item}")

                elif side == 'left':
                    print("Parent node: %s contains data on the left" % parent)

                if side == 'right' and parentnode.right is None:
                    parentnode.right = node
                    self.size += 1
                    print(f"New node added. Parent: {parentnode.data}, Left Child: {item}")

                elif side == 'right':
                    print("Parent node: %s contains data on the right" % parent)
                    

    def replace(self, item, new_item):
        """Precondition: item is in self.
        Raises: KeyError if item is not in self.
        postcondition: item is replaced by new_item."""

        if self.find(item) is not None:
            oldnode = self.find(item)
            oldnode.data = new_item
            print(f"{item} replace by {new_item}")
        else:
            raise KeyError("%s is not in the tree" % item)


def main():
    tree = LinkedBT()

    tree.add("A")
    tree.add("B", "A")
    tree.add("C", "A", "right")
    tree.add("D", "A")
    tree.add("D", "A", "right")
    tree.add("D", "X")
    tree.add("D", "B", "right")
    tree.add("E", "D")
    tree.add("F", "C")
    tree.add("G", "C")

    print("\nString:\n" + str(tree))
    print("Tree size:", len(tree))

    for item in tree:
        print(item, end=' ')
    print()

    tree.replace('E', 'G')
    print(tree)

    tree.clear()
    print("Clear tree")
    print("Tree size:", tree.size)


if __name__ == "__main__":
    main()
