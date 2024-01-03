class Vertex:

    def __init__(self, val):
        self.Value = val


class SimpleGraph:

    def __init__(self, size):
        self.max_vertex = size  # максимальное количество вершин
        self.m_adjacency = [[0] * size for _ in range(size)]  # матрица смежности 0 и 1
        self.vertex = [None] * size  # список вершин. по индексу поиск вершины и связи с другими по матрице

    def AddVertex(self, v):
        ix = -1
        if None in self.vertex:
            ix = self.vertex.index(None)
            self.vertex[ix] = Vertex(v)
        return ix

    # здесь и далее, параметры v -- индекс вершины в списке  vertex

    def RemoveVertex(self, v):
        # ваш код удаления вершины со всеми её рёбрами
        if v >= self.max_vertex:
            return False
        for v2 in range(self.max_vertex):
            if self.IsEdge(v, v2):
                self.RemoveEdge(v, v2)
        self.vertex[v] = None
        return True

    def IsEdge(self, v1, v2):
        # True если есть ребро между вершинами v1 и v2
        if all([v1 < self.max_vertex, v2 < self.max_vertex]):
            return self.m_adjacency[v1][v2] == 1
        return False

    def AddEdge(self, v1, v2):
        # добавление ребра между вершинами v1 и v2
        if all([v1 < self.max_vertex, v2 < self.max_vertex]):
            self.m_adjacency[v1][v2], self.m_adjacency[v2][v1] = 1, 1
            return True
        return False

    def RemoveEdge(self, v1, v2):
        # удаление ребра между вершинами v1 и v2
        if all([v1 < self.max_vertex, v2 < self.max_vertex]):
            self.m_adjacency[v1][v2], self.m_adjacency[v2][v1] = 0, 0
            return True
        return False