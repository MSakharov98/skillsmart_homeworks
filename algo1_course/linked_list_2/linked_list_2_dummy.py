class Node:
    def __init__(self, v):
        self.value = v
        self.prev = None
        self.next = None

class DummyLinkedList2:
    def __init__(self):
        self.dummy_head = Node(None)
        self.dummy_tail = Node(None)
        self.dummy_head.next = self.dummy_tail
        self.dummy_tail.prev = self.dummy_head

    def add_in_tail(self, item):
        item.prev = self.dummy_tail.prev
        item.next = self.dummy_tail
        self.dummy_tail.prev.next = item
        self.dummy_tail.prev = item

    def find(self, val):
        current = self.dummy_head.next
        while current != self.dummy_tail:
            if current.value == val:
                return current
            current = current.next
        return None

    def find_all(self, val):
        result = []
        current = self.dummy_head.next
        while current != self.dummy_tail:
            if current.value == val:
                result.append(current)
            current = current.next
        return result

    def delete(self, val, all=False):
        current = self.dummy_head.next
        while current != self.dummy_tail:
            if current.value == val:
                current.prev.next = current.next
                current.next.prev = current.prev
                if not all:
                    return
            current = current.next

    def clean(self):
        self.dummy_head.next = self.dummy_tail
        self.dummy_tail.prev = self.dummy_head

    def len(self):
        count = 0
        current = self.dummy_head.next
        while current != self.dummy_tail:
            count += 1
            current = current.next
        return count

    def insert(self, afterNode, newNode):
        newNode.prev = afterNode
        newNode.next = afterNode.next
        afterNode.next.prev = newNode
        afterNode.next = newNode

    def add_in_head(self, newNode):
        newNode.next = self.dummy_head.next
        newNode.prev = self.dummy_head
        self.dummy_head.next.prev = newNode
        self.dummy_head.next = newNode
