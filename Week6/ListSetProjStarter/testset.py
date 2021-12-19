"""
File: testbag.py
Author: Ken Lambert
A tester program for bag implementations.
"""

from listset import ListSet

def test(setType):
    """Expects a bag type as an argument and runs some tests
    on objects of that type."""
    print("Testing", setType)
    lyst = list(range(1, 11))
    print("The list of items added is:", lyst)
    b = setType(lyst)
    print("The set's size:", len(b))
    print("The set's string:", b)
    print("The set is empty:", b.isEmpty())
    print("4 is in the set:", 4 in b)
    print("0 is in the set:", 0 in b)
    b.add(7)
    print("Add 7 in set")
    print("The set's string:", b)
    b.remove(10)
    print("Remove 10 from set")
    print("The set's string:", b)
    c = ListSet(b)
    print("c = ListSet(b)")
    print("b == c?", b == c)
    d = ListSet([22, 4])
    print("d = ListSet(22, 4)")
    print("b == d?", b == d)
    e = b + d
    print("e = b + d")
    print("set e's string:", e)
    c.clear()
    print("c.clear()")
    print("set c's string:", c)


test(ListSet)
