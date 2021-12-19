"""
File: testsortedbag.py
Author: Man-Chi Leung
A tester program for sorted bag implementations.
"""

from listsortedbag import ListSortedBag


def test(bagType):
    """Expects a bag type as an argument and runs some tests
    on objects of that type."""
    print("Testing", bagType)
    lyst = [8, 2, 4, 7, 6, 1]
    print("The list of items added is:", lyst)
    b = bagType(lyst)
    print("The bag's size:", len(b))
    print("The bag's string:", b)
    print()
    print("Searching for 6")
    print("6 is in the bag:", 6 in b)
    print()
    print("Searching for 3")
    print("3 is in the bag:", 3 in b)
    print()
    print("Add 5 in bag")
    b.add(5)
    print("The bag's string:", b)
    print()
    print("Remove 4 from bag")
    b.remove(4)
    print("The bag's string:", b)
    print()
    print("c = ListSortedBag(b)")
    c = ListSortedBag(b)
    print("b == c?", b == c)
    print()
    print("d = ListSortedBag(3, 4)")
    d = ListSortedBag([3, 4])
    print("b == d?", b == d)
    print()
    print("e = b + d")
    e = b + d
    print("bag e's string:", e)


test(ListSortedBag)
