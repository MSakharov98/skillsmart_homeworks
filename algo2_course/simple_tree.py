class SimpleTreeNode:

    def __init__(self, val, parent):
        self.NodeValue = val  # значение в узле
        self.Parent = parent  # родитель или None для корня
        self.Children = []  # список дочерних узлов
        self.Level = None
        self.NodesCountInSubtree = 0


class SimpleTree:

    def __init__(self, root):
        self.Root = root  # корень, может быть None

    def AddChild(self, ParentNode, NewChild):
        ParentNode.Children.append(NewChild)
        NewChild.Parent = ParentNode

    def DeleteNode(self, NodeToDelete):
        isRoot = (self.Root == NodeToDelete)
        if isRoot: return
        ParentNode = NodeToDelete.Parent
        if ParentNode is not None:
            ParentNode.Children.remove(NodeToDelete)
        NodeToDelete.Parent = None

    def GetAllNodes(self):
        if self.Root is None: return []

        nodesList = [self.Root]
        currentNodeIndex = 0
        while (currentNodeIndex < len(nodesList)):
            node = nodesList[currentNodeIndex]
            nodesList += node.Children
            currentNodeIndex += 1
        return nodesList

    def FindNodesByValue(self, val):
        if self.Root is None: return []

        result = []
        nodesList = [self.Root]
        currentNodeIndex = 0
        while (currentNodeIndex < len(nodesList)):
            node = nodesList[currentNodeIndex]
            if node.NodeValue == val: result.append(node)
            nodesList += node.Children
            currentNodeIndex += 1
        return result

    def MoveNode(self, OriginalNode, NewParent):
        originalParent = OriginalNode.Parent
        originalParent.Children.remove(OriginalNode)
        OriginalNode.Parent = NewParent
        NewParent.Children.append(OriginalNode)

    def Count(self):
        return len(self.GetAllNodes())

    def isLeaf(self, node):
        return node.Children == []

    def LeafCount(self):
        if self.Root is None: return []

        leafCount = 0
        nodesList = [self.Root]
        currentNodeIndex = 0
        while (currentNodeIndex < len(nodesList)):
            node = nodesList[currentNodeIndex]
            if self.isLeaf(node): leafCount += 1
            nodesList += node.Children
            currentNodeIndex += 1
        return leafCount

    def AssignLevelToNodes(self):
        if self.Root is None: return []
        nodesList = [self.Root]
        currentNodeIndex = 0
        while (currentNodeIndex < len(nodesList)):
            node = nodesList[currentNodeIndex]
            node.Level = 0 if node.Parent is None else node.Parent.Level + 1
            nodesList += node.Children
            currentNodeIndex += 1
        return nodesList

    def GetNodesCountInSubtree(self, node: SimpleTreeNode):
        if node is None: return 0
        if self.isLeaf(node): return 1
        nodesCount = 1
        for child in node.Children:
            nodesCount += self.GetNodesCountInSubtree(child)
        node.NodesCountInSubtree = nodesCount
        return nodesCount

    def EvenTrees(self):
        result = []
        if self.Root is None:
            return []
        self.GetNodesCountInSubtree(self.Root)
        if self.Root.NodesCountInSubtree % 2 != 0:
            return []
        nodesList = [self.Root]
        currentNodeIndex = 0
        while (currentNodeIndex < len(nodesList)):
            node = nodesList[currentNodeIndex]
            if node.NodesCountInSubtree != 0 and node.NodesCountInSubtree % 2 == 0 and \
                    node.Parent is not None:
                result.append(node.Parent)
                result.append(node)
            nodesList += node.Children
            currentNodeIndex += 1
        return result

        return []