class BSTNode:

    def __init__(self, key, val, parent):
        self.NodeKey = key  # ключ узла
        self.NodeValue = val  # значение в узле
        self.Parent = parent  # родитель или None для корня
        self.LeftChild = None  # левый потомок
        self.RightChild = None  # правый потомок


class BSTFind:  # промежуточный результат поиска

    def __init__(self):
        self.Node = None  # None если
        # в дереве вообще нету узлов

        self.NodeHasKey = False  # True если узел найден
        self.ToLeft = False  # True, если родительскому узлу надо
        # добавить новый узел левым потомком


class BST:

    def __init__(self, node):
        self.Root = node  # корень дерева, или None
        self.size = 0 if node is None else 1

    def find_node_by_key_recursively(self, subtree_root, key):
        if key == subtree_root.NodeKey:
            result = BSTFind()
            result.Node = subtree_root
            result.NodeHasKey = True
            return result
        elif key < subtree_root.NodeKey and subtree_root.LeftChild is None:
            result = BSTFind()
            result.Node = subtree_root
            result.ToLeft = True
            return result
        elif key > subtree_root.NodeKey and subtree_root.RightChild is None:
            result = BSTFind()
            result.Node = subtree_root
            result.ToLeft = False
            return result
        elif key < subtree_root.NodeKey and subtree_root.LeftChild is not None:
            return self.find_node_by_key_recursively(subtree_root.LeftChild, key)
        elif key > subtree_root.NodeKey and subtree_root.RightChild is not None:
            return self.find_node_by_key_recursively(subtree_root.RightChild, key)

    def FindNodeByKey(self, key):
        if self.Root is None:
            return BSTFind()
        return self.find_node_by_key_recursively(self.Root, key)

    def AddKeyValue(self, key, val):
        if self.Root is None:
            self.Root = BSTNode(key, val, None)
            self.size += 1
            return True
        search_result = self.FindNodeByKey(key)
        if search_result.NodeHasKey:
            return False
        new_node = BSTNode(key, val, search_result.Node)
        if search_result.ToLeft:
            search_result.Node.LeftChild = new_node
        else:
            search_result.Node.RightChild = new_node
        self.size += 1
        return True

    def find_min_max_recursively(self, from_node, find_max):
        if find_max and from_node.RightChild is not None:
            return self.find_min_max_recursively(from_node.RightChild, find_max)
        elif not find_max and from_node.LeftChild is not None:
            return self.find_min_max_recursively(from_node.LeftChild, find_max)
        return from_node

    def FinMinMax(self, FromNode, FindMax):
        if FromNode is None:
            return None
        return self.find_min_max_recursively(FromNode, FindMax)

    def resolve_successor(self, successor, node_to_delete):
        parent = successor.Parent
        successor.LeftChild = node_to_delete.LeftChild
        node_to_delete.LeftChild.Parent = successor
        if parent is node_to_delete:
            return
        parent.LeftChild = successor.RightChild
        if successor.RightChild is not None:
            successor.RightChild.Parent = parent
        successor.RightChild = node_to_delete.RightChild
        node_to_delete.RightChild.Parent = successor

    def insert_at_parent(self, parent, new_child, to_left):
        if to_left is None:
            self.Root = new_child
        elif to_left:
            parent.LeftChild = new_child
        else:
            parent.RightChild = new_child
        if new_child is not None:
            new_child.Parent = parent

    def DeleteNodeByKey(self, key):
        to_delete_result = self.FindNodeByKey(key)
        node_to_delete = to_delete_result.Node
        if node_to_delete is None or not to_delete_result.NodeHasKey:
            return False
        to_left = None
        if node_to_delete is not self.Root:
            to_left = node_to_delete is node_to_delete.Parent.LeftChild
        if node_to_delete.LeftChild is None and node_to_delete.RightChild is not None:
            self.insert_at_parent(node_to_delete.Parent, node_to_delete.RightChild, to_left)
        elif node_to_delete.LeftChild is not None and node_to_delete.RightChild is None:
            self.insert_at_parent(node_to_delete.Parent, node_to_delete.LeftChild, to_left)
        elif node_to_delete.LeftChild is None and node_to_delete.RightChild is None:
            self.insert_at_parent(node_to_delete.Parent, None, to_left)
        else:
            successor = self.FinMinMax(node_to_delete.RightChild, False)
            self.resolve_successor(successor, node_to_delete)
            self.insert_at_parent(node_to_delete.Parent, successor, to_left)
        self.size -= 1
        return True

    def Count(self):
        return self.size  # количество узлов в дереве

    def WideAllNodes(self):
        result = []
        queue = []
        if self.Root is not None:
            queue.append(self.Root)
        while len(queue) > 0:
            current_node = queue.pop()
            result.append(current_node)
            if current_node.LeftChild is not None:
                queue.insert(0, current_node.LeftChild)
            if current_node.RightChild is not None:
                queue.insert(0, current_node.RightChild)
        return tuple(result)

    def recursive_deep_all_nodes(self, subtree_root, order, result):
        if subtree_root is None:
            return
        if order == 2:
            result.append(subtree_root)
        self.recursive_deep_all_nodes(subtree_root.LeftChild, order, result)
        if order == 0:
            result.append(subtree_root)
        self.recursive_deep_all_nodes(subtree_root.RightChild, order, result)
        if order == 1:
            result.append(subtree_root)

    def DeepAllNodes(self, order):
        result = []
        self.recursive_deep_all_nodes(self.Root, order, result)
        return tuple(result)