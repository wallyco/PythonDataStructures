"""
File: teststack.py
Author: Man-Chi Leung
A tester program for queue implementation.
"""

from listqueue import ListQueue


def test(queueType):
    """Expects a queue type as an argument and runs some tests
    on objects of that type."""
    print("Testing", queueType)
    lyst = [8, 2, 4, 7, 6, 1]
    print("The list of items added is:", lyst)
    b = queueType(lyst)
    print("The queue's size:", len(b))
    print("The queue's string:", b)
    print()

    print("Add 5")
    b.add(5)
    print("The queue's string:", b)
    print()
    print("Peek")
    print("Item at front of the queue:", b.peek())
    print("The queue's string:", b)
    print()
    print("Pop")
    print("Item popped:", b.pop())
    print("The queue's string:", b)
    print()
    print("c = ListQueue(b)")
    c = ListQueue(b)
    print("b == c?", b == c)
    print()
    print("d = ListQueue([1, 2, 3, 4, 5, 6])")
    d = ListQueue([1, 2, 3, 4, 5, 6])
    print("b == d?", b == d)
    print()
    print("e = b + d")
    e = b + d
    print("Queue e's string:", e)
    print("Is e empty?", e.isEmpty())
    e.clear()
    print("Clear e")
    print("Is e empty?", e.isEmpty())
    print("The queue's string:", e)


test(ListQueue)
