"""
File: teststack.py
Author: Man-Chi Leung
A tester program for stack implementation.
"""

from liststack import ListStack


def test(stackType):
    """Expects a stack type as an argument and runs some tests
    on objects of that type."""
    print("Testing", stackType)
    lyst = [8, 2, 4, 7, 6, 1]
    print("The list of items added is:", lyst)
    b = stackType(lyst)
    print("The stack's size:", len(b))
    print("The stack's string:", b)
    print()

    print("Push 5")
    b.push(5)
    print("The stack's string:", b)
    print()
    print("Peek")
    print(b.peek())
    print("The stack's string:", b)
    print()
    print("Pop")
    print("Item popped:", b.pop())
    print("The stack's string:", b)
    print()
    print("c = ListStack(b)")
    c = ListStack(b)
    print("b == c?", b == c)
    print()
    print("d = ListStack([1, 2, 3, 4, 5, 6])")
    d = ListStack([1, 2, 3, 4, 5, 6])
    print("b == d?", b == d)
    print()
    print("e = b + d")
    e = b + d
    print("Stack e's string:", e)
    print("Is e empty?", e.isEmpty())
    e.clear()
    print("Clear e")
    print("Is e empty?", e.isEmpty())
    print("The stack's string:", e)

test(ListStack)
