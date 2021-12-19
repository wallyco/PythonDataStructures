"""
File: linked_list.py

Add an insert and a remove function.

Tests the Node class.
"""

from node import Node


def length(head):
    """Returns the number of items in the linked structure
    referred to by head."""
    probe = head
    count = 0
    while probe is not None:
        count += 1
        probe = probe.next
    return count


def insert(index, newItem, head):
    """Inserts newItem at position is the linked structure
    referred to by head.  Returns a reference to the new
    structure."""

    nn = Node(newItem)
    cur = head
    if head is None:
        cur = nn
        return cur
    else:
        i = 0
        if index == 0:
            nn.next = cur
            cur = nn
            return cur
        else:
            if index != 1:
                while ((i + 1) != index) and cur.next is not None:
                    cur = cur.next
                    i += 1
            nn.next = cur.next
            cur.next = nn
    return head


def remove(index, head):
    """Removes the item at index from the linked structure
    referred to by head and returns the tuple (head, item)
    Precondition: 0 <= index < length(head)"""
    cur = head

    if index < 0 or index > length(head):
        raise IndexError("Index out of bounds (Index: %s" % index)
    else:
        cur = head
        nodebefore = head
        i = 0
        while i != index:
            if i > 0:
                nodebefore = cur

            if cur.next is not None and index > i:
                cur = cur.next
            i += 1
        if index == 0:
            head = cur.next
        elif index == length(head):
            nodebefore.next = None
        else:
            nodebefore.next = cur.next
        return head, head.data


def printStructure(head):
    """Prints the items in the structure referred to by head."""
    probe = head
    while probe is not None:
        print(probe.data, end=" ")
        probe = probe.next
    print()


def main():
    """Tests modifications."""
    head = None

    head = insert(0, "1", head)
    print("Insert 1 at index 0:", end=" ")
    printStructure(head)

    head = insert(1, "2", head)
    print("Insert 2 at index 1:", end=" ")
    printStructure(head)

    head = insert(0, "0", head)
    print("Insert 0 at index 0:", end=" ")
    printStructure(head)

    head = insert(3, "3", head)
    print("Insert 3 at index 3:", end=" ")
    printStructure(head)

    head = insert(1, "9", head)
    print("Insert 9 at index 1:", end=" ")
    printStructure(head)

    (head, item) = remove(0, head)
    print("First element removed:", end=" ")
    printStructure(head)

    (head, item) = remove(0, head)
    print("First element removed:", end=" ")
    printStructure(head)

    (head, item) = remove(length(head) - 1, head)
    print("Last element removed:", end=" ")
    printStructure(head)

    (head, item) = remove(1, head)
    print("Second element removed:", end=" ")
    printStructure(head)


if __name__ == "__main__": main()
