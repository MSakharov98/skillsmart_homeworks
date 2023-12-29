class BSTNode:

    def __init__(self, key, parent):
        self.NodeKey = key  # ключ узла
        self.Parent = parent  # родитель или None для корня
        self.LeftChild = None  # левый потомок
        self.RightChild = None  # правый потомок
        self.Level = 0  # уровень узла


class BalancedBST:

    def __init__(self):
        self.Root = None  # корень дерева

    def MakeNode(self, a, startIndex, endIndex, depth):
        if endIndex < startIndex:
            return None
        if endIndex - startIndex == 0:
            leaf = BSTNode(key=a[startIndex], parent=None)
            leaf.Level = depth
            return leaf
        parentIndex = startIndex + (endIndex - startIndex) // 2
        parent = BSTNode(key=a[parentIndex], parent=None)
        leftChild = self.MakeNode(a, startIndex, parentIndex - 1, depth + 1)
        rightChild = self.MakeNode(a, parentIndex + 1, endIndex, depth + 1)
        parent.LeftChild = leftChild
        parent.RightChild = rightChild
        parent.Level = depth
        if leftChild is not None:
            leftChild.Parent = parent
        if rightChild is not None:
            rightChild.Parent = parent

        return parent

    def GenerateTree(self, a):
        sortedArr = a.copy()
        sortedArr.sort()
        node = self.MakeNode(sortedArr, 0, len(sortedArr) - 1, 0)
        self.Root = node

    def CheckBalanceAndDepth(self, root_node):
        if root_node is None:
            return True, 0

        isLeftSubtreeBalanced, leftSubTreeDepth = self.CheckBalanceAndDepth(root_node.LeftChild)
        if not isLeftSubtreeBalanced: return False, leftSubTreeDepth + 1

        isRightSubtreeBalanced, rightSubTreeDepth = self.CheckBalanceAndDepth(root_node.RightChild)
        if not isRightSubtreeBalanced: return False, max(rightSubTreeDepth, leftSubTreeDepth) + 1

        isBalanced = True
        if abs(leftSubTreeDepth - rightSubTreeDepth) > 1:
            isBalanced = False
        return isBalanced, max(rightSubTreeDepth, leftSubTreeDepth) + 1

    def IsBalanced(self, root_node):
        isBalanced, _ = self.CheckBalanceAndDepth(root_node)
        return isBalanced