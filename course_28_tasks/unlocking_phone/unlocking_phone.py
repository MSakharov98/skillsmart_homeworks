def PatternUnlock(N, hits):
    def distance(x1, y1, x2, y2):
        dx = abs(x2 - x1)
        dy = abs(y2 - y1)
        if dx == 1 and dy == 0:
            return 1
        elif dx == 0 and dy == 1:
            return 1
        elif dx == 1 and dy == 1:
            return 1.41421
        elif dx == 2 and dy == 0:
            return 2
        elif dx == 0 and dy == 2:
            return 2
        elif dx == 2 and dy == 1:
            return 2.23607
        elif dx == 1 and dy == 2:
            return 2.23607
        else:
            return ((dx ** 2 + dy ** 2) ** 0.5)

    coords = {
        1: (0, 1), 2: (1, 1), 3: (2, 1),
        4: (0, 2), 5: (1, 2), 6: (2, 2),
        7: (0, 3), 8: (1, 3), 9: (2, 3)
    }

    length = 0
    for i in range(N - 1):
        x1, y1 = coords[hits[i]]
        x2, y2 = coords[hits[i + 1]]
        length += distance(x1, y1, x2, y2)

    result = '{:.5f}'.format(length).rstrip('0').replace('.', '')

    return result

