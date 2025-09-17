class SimpleTreeNode:

    def __init__(self, val, parent):
        self.NodeValue = val  # значение в узле
        self.Parent = parent  # родитель или None для корня
        self.Children = []  # список дочерних узлов


class SimpleTree:

    def __init__(self, root):
        self.Root = root  # корень, может быть None

    def AddChild(self, ParentNode, NewChild):
        if ParentNode is None:
            self.Root = NewChild
        else:
            ParentNode.Children.append(NewChild)
            NewChild.Parent = ParentNode

    def DeleteNode(self, NodeToDelete):
        if NodeToDelete.Parent is None:
            return
        NodeToDelete.Parent.Children.remove(NodeToDelete)
        NodeToDelete.Parent = None

    @staticmethod
    def subnodes(acc, children, val=None, find=False):
        if not find:
            acc.extend(children)
            for child in children:
                SimpleTree.subnodes(acc, child.Children)
        else:
            for child in children:
                if child.NodeValue == val:
                    acc.append(child)
                SimpleTree.subnodes(acc, child.Children, val, find=True)

    def GetAllNodes(self):
        if self.Root is None:
            return []
        nodes = [self.Root]
        SimpleTree.subnodes(nodes, self.Root.Children)
        return nodes

    def FindNodesByValue(self, val):
        if self.Root is None:
            return []
        nodes = [self.Root] if self.Root.NodeValue == val else []
        SimpleTree.subnodes(nodes, self.Root.Children, val, find=True)
        return nodes

    def MoveNode(self, OriginalNode, NewParent):
        if OriginalNode == self.Root:
            return
        self.DeleteNode(OriginalNode)
        self.AddChild(NewParent, OriginalNode)

    def Count(self):
        # количество всех узлов в дереве
        return len(self.GetAllNodes())

    def LeafCount(self):
        # количество листьев в дереве
        return sum([1 for node in self.GetAllNodes() if len(node.Children) == 0])

    def EvenTrees(self):
        if self.Root is None or self.Count() % 2 != 0:
            return []

        edges = []
        check = [self.Root]

        while len(check) > 0:
            node = check.pop(0)
            for child in node.Children:
                check.append(child)
                nodes = [child]
                SimpleTree.subnodes(nodes, child.Children)
                if len(nodes) % 2 == 0:
                    edges.append(node)
                    edges.append(child)
        return edges