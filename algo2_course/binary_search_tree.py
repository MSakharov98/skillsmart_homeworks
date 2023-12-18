from typing import List


class BSTNode:

    def __init__(self, key, val, parent):
        self.NodeKey = key
        self.NodeValue = val
        self.Parent = parent
        self.LeftChild = None
        self.RightChild = None


class BSTFind:

    def __init__(self):
        self.Node = None

        self.NodeHasKey = False
        self.ToLeft = False


class BST:

    def __init__(self, node):
        self.Root = node

    def FindNodeByKey(self, key):

        found_node = BSTFind()

        if self.Root is None:
            return found_node

        def traverseTree(node: BSTNode, parentNode):
            if node is None:
                found_node.Node = parentNode
                found_node.NodeHasKey = False
                found_node.ToLeft = True if key < parentNode.NodeKey else False
                return

            if node.NodeKey == key:
                found_node.Node = node
                found_node.NodeHasKey = True
                return

            traverseTree(node.LeftChild if key < node.NodeKey else node.RightChild, node)

        traverseTree(self.Root, None)

        return found_node

    def AddKeyValue(self, key, val):
        found_node = self.FindNodeByKey(key)

        if found_node.NodeHasKey:
            return False

        if self.Root is None:
            self.Root = BSTNode(key, val, None)
            return True

        def traverseTree(node: BSTNode, parent_key):
            if node is None:
                return

            if node.NodeKey == parent_key:
                if found_node.ToLeft:
                    node.LeftChild = BSTNode(key, val, node)
                else:
                    node.RightChild = BSTNode(key, val, node)
                return

            traverseTree(node.LeftChild if parent_key < node.NodeKey else node.RightChild, parent_key)

        traverseTree(self.Root, found_node.Node.NodeKey)

        return True

    def FinMinMax(self, FromNode, FindMax):
        node_to_start = None

        if self.Root is None:
            return None

        if FromNode:
            def get_node(node: BSTNode):
                if node is None:
                    return None

                if node.NodeKey == FromNode.NodeKey:
                    return node

                return get_node(node.LeftChild if FromNode.NodeKey < node.NodeKey else node.RightChild)

            node_to_start = get_node(self.Root)

            if node_to_start is None:
                return None

        def traverseTree(node: BSTNode):
            if (FindMax and node.RightChild is None) or (not FindMax and node.LeftChild is None):
                return node

            return traverseTree(node.RightChild if FindMax else node.LeftChild)

        return traverseTree(node_to_start or self.Root)

    def DeleteNodeByKey(self, key):

        def getNodeToMove(node: BSTNode):
            if (node.LeftChild is None and node.RightChild is None) or (node.LeftChild is None and node.RightChild):
                if node.Parent.LeftChild and node.Parent.LeftChild.NodeKey == node.NodeKey:
                    node.Parent.LeftChild = None
                if node.Parent.RightChild and node.Parent.RightChild.NodeKey == node.NodeKey:
                    node.Parent.RightChild = None
                return node

            return getNodeToMove(node.LeftChild)

        if self.Root is None:
            return False

        if self.Root.LeftChild is None and self.Root.RightChild is None:
            if self.Root.NodeKey == key:
                self.Root = None
                return True
            if self.Root.NodeKey != key:
                return False

        def traverseTree(node: BSTNode):
            if node is None:
                return False

            if node.NodeKey == key:
                if node.LeftChild and node.RightChild:
                    node_to_move = getNodeToMove(node.RightChild)
                    node_to_move.Parent = node.Parent
                    if node.RightChild and node.RightChild.NodeKey != node_to_move.NodeKey:
                        node_to_move.RightChild = node.RightChild
                        node_to_move.RightChild.Parent = node_to_move
                    if node.LeftChild and node.LeftChild.NodeKey != node_to_move.NodeKey:
                        node_to_move.LeftChild = node.LeftChild
                        node_to_move.LeftChild.Parent = node_to_move
                    if self.Root is None or self.Root.NodeKey == node.NodeKey:
                        self.Root = node_to_move
                        return True
                    if node.Parent and node.Parent.LeftChild.NodeKey == node.NodeKey:
                        node.Parent.LeftChild = node_to_move
                        return True
                    if node.Parent and node.Parent.RightChild.NodeKey == node.NodeKey:
                        node.Parent.RightChild = node_to_move
                        return True

                if node.LeftChild or node.RightChild:
                    if node.LeftChild:
                        node.LeftChild.Parent = node.Parent
                        if not node.Parent:
                            self.Root = node.LeftChild
                            return True
                    if node.RightChild:
                        node.RightChild.Parent = node.Parent
                        if not node.Parent:
                            self.Root = node.RightChild
                            return True

                    if node.Parent.LeftChild.NodeKey == node.NodeKey:
                        node.Parent.LeftChild = node.LeftChild or node.RightChild
                        return True
                    if node.Parent.RightChild.NodeKey == node.NodeKey:
                        node.Parent.RightChild = node.LeftChild or node.RightChild
                        return True

                if node.Parent.LeftChild and node.NodeKey == node.Parent.LeftChild.NodeKey:
                    node.Parent.LeftChild = None
                if node.Parent.RightChild and node.NodeKey == node.Parent.RightChild.NodeKey:
                    node.Parent.RightChild = None
                return True

            return traverseTree(node.LeftChild if key < node.NodeKey else node.RightChild)

        return traverseTree(self.Root)

    def Count(self):
        count = [0]

        def traverseTree(node: BSTNode):
            if node is None:
                return

            traverseTree(node.LeftChild)
            count[0] += 1
            traverseTree(node.RightChild)

        traverseTree(self.Root)

        return count[0]

    def WideAllNodes(self):
        result = ()
        queue = [self.Root] if self.Root else []

        while len(queue) > 0:
            node = queue.pop(0)
            result += (node,)

            if node.LeftChild:
                queue.append(node.LeftChild)
            if node.RightChild:
                queue.append(node.RightChild)

        return result

    def DeepAllNodes(self, order):
        result = ()

        def traverse(node):
            nonlocal result
            if node is None:
                return

            if order == 0:
                traverse(node.LeftChild)
                result += (node,)
                traverse(node.RightChild)

            if order == 1:
                traverse(node.LeftChild)
                traverse(node.RightChild)
                result += (node,)

            if order == 2:
                result += (node,)
                traverse(node.LeftChild)
                traverse(node.RightChild)

        traverse(self.Root)

        return result