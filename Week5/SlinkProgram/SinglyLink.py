class Node(object):
    def __init__(self, data, next=None):
        """Instantiates a Node with a default next of None."""
        self.data = data
        self.next = next

    def getItem(self):
        return self.data

    def getNext(self):
        return self.next

    def setNext(self, newNext):
        self.next = newNext


class LinkedList(object):
    def __init__(self, head=None):
        self.head = head

    def insert(self, item, position=0):
        nn = Node(item)

        if self.head is None:
            self.head = nn

        elif position > 0:
            last = self.head
            while range(position, 1):
                last = last.next
            last.next = nn
        else:
            nn.next
            self.head.next = nn

    def toString(self):
        node = self.head
        while node:
            print(node.data)
            node = node.next


def main():
    ll = LinkedList()
    ll.insert(1, 0)
    print("Insert %s at index %s:" % (1, 0))
    ll.toString()
    ll.insert(2, 1)
    print("Insert %s at index %s:" % (2, 1))
    ll.toString()
    ll.insert(0, 0)
    print("Insert %s at index %s:" % (0, 0))
    ll.toString()
    ll.insert(3, 3)
    print("Insert %s at index %s:" % (3, 3))
    ll.toString()



if __name__ == "__main__":
    main()
