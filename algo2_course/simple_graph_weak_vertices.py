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

    def WeakVertices(self):
        # возвращает список узлов вне треугольников

        isWeak = [False] * self.max_vertex
        for v in range(self.max_vertex):
            if sum(self.m_adjacency[v]) < 2:
                isWeak[v] = True
            elif sum(self.m_adjacency[v]) == 2:
                if self.IsEdge(v, v):
                    isWeak[v] = True
                else:
                    v1 = self.m_adjacency[v].index(1)
                    v2 = self.m_adjacency[v].index(1, v1 + 1)
                    if not self.IsEdge(v1, v2) or not self.IsEdge(v2, v1):
                        isWeak[v] = True
            else:
                adj = []
                for ix, val in enumerate(self.m_adjacency[v]):
                    if val < 1:
                        continue
                    adj.append(ix)
                flag = False
                for av1 in adj:
                    for av2 in adj:
                        if av1 == av2:
                            continue
                        if self.IsEdge(av1, av2):
                            flag = True
                            break
                    if flag:
                        break
                if not flag:
                    isWeak[v] = True
        result = []
        for i in range(self.max_vertex):
            if isWeak[i]:
                result.append(self.vertex[i])

        return result