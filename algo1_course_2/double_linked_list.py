class Node:
    def __init__(self, v):
        self.value = v
        self.prev = None
        self.next = None

class LinkedList2:
    def __init__(self):
        self.head = None
        self.tail = None

    def add_in_tail(self, item):
        if self.head is None:
            self.head = item
            item.prev = None
            item.next = None
        else:
            self.tail.next = item
            item.prev = self.tail
        self.tail = item

    def find(self, val):
        current = self.head
        while current is not None:
            if current.value == val:
                return current
            current = current.next
        return None

    def find_all(self, val):
        result = []
        current = self.head
        while current is not None:
            if current.value == val:
                result.append(current)
            current = current.next
        return result

    def delete(self, val, all=False):
        current = self.head
        while current is not None:
            if current.value == val:
                if current.prev is not None:
                    current.prev.next = current.next
                else:
                    self.head = current.next

                if current.next is not None:
                    current.next.prev = current.prev
                else:
                    self.tail = current.prev

                if not all:
                    return
            current = current.next

    def clean(self):
        self.head = None
        self.tail = None

    def len(self):
        count = 0
        current = self.head
        while current is not None:
            count += 1
            current = current.next
        return count

    def insert(self, afterNode, newNode):
        if afterNode is None:
            if self.head is None:
                self.head = newNode
                self.tail = newNode
                newNode.prev = None
                newNode.next = None
            else:
                newNode.prev = self.tail
                newNode.next = None
                self.tail.next = newNode
                self.tail = newNode
        else:
            newNode.prev = afterNode
            newNode.next = afterNode.next
            if afterNode.next is not None:
                afterNode.next.prev = newNode
            afterNode.next = newNode

            if self.tail == afterNode:
                self.tail = newNode

    def add_in_head(self, newNode):
        if self.head is None:
            self.head = newNode
            self.tail = newNode
            newNode.prev = None
            newNode.next = None
        else:
            newNode.next = self.head
            newNode.prev = None
            self.head.prev = newNode
            self.head = newNode
