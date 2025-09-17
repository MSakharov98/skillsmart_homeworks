class Node:
    def __init__(self, v):
        self.value = v
        self.prev = None
        self.next = None


class OrderedList:
    def __init__(self, asc):
        self.head = None
        self.tail = None
        self.__ascending = asc

    def compare(self, v1, v2):
        if v1 < v2:
            return -1
        elif v1 == v2:
            return 0
        else:
            return 1

    def add(self, value):
        new_node = Node(value)

        if self.head is None:
            self.head = new_node
            new_node.prev = None
            new_node.next = None
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
        self.tail = new_node

        task = True
        node = self.head

        while task is True:
            task = False
            while node is not None and node.next is not None:
                if node.value > node.next.value and self.__ascending:
                    data = node.value
                    node.value = node.next.value
                    node.next.value = data
                    task = True
                elif node.value < node.next.value and not self.__ascending:
                    data = node.next.value
                    node.next.value = node.value
                    node.value = data
                    task = True
                node = node.next
            node = self.head

    def find(self, val):
        node = self.head
        while node is not None:
            if node.value == val:
                return node
            elif node.value > val and self.__ascending:
                return None
            elif node.value < val and not self.__ascending:
                return None
            node = node.next

    def delete(self, val):
        node = self.head
        if node is None:
            return
        elif node.value == val:
            self.head = node.next
            if node.next is None:
                self.tail = None
            else:
                self.head.prev = None
            return
        else:
            while node is not None:
                if node.value == val and node.next is not None:
                    node.prev.next = node.next
                    node.next.prev = node.prev
                    break
                elif node.value == val and node.next is None:
                    self.tail = self.tail.prev
                    self.tail.next = None
                    return
                node = node.next

    def clean(self, asc):
        self.__ascending = asc
        self.head = None
        self.tail = None

    def len(self):
        count = 0
        node = self.head
        while node is not None:
            count += 1
            node = node.next
        return count

    def get_all(self):
        r = []
        node = self.head
        while node is not None:
            r.append(node)
            node = node.next
        return r

class OrderedStringList(OrderedList):
    def __init__(self, asc):
        super(OrderedStringList, self).__init__(asc)

    def compare(self, v1, v2):
        v1 = v1.strip()
        v2 = v2.strip()
        if v1 < v2:
            return -1
        elif v1 == v2:
            return 0
        else:
            return 1