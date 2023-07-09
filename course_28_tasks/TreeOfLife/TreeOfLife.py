def TreeOfLife(H, W, N, tree):

    work_tree = []

    for a in range(len(tree)):
        tree[a] = list(tree[a])
        branch = []
        for b in range(len(tree[a])):
            if tree[a][b] == '.':
                branch.append(0)
            elif tree[a][b] == '+':
                branch.append(1)

        work_tree.append(branch)

    for z in range(N):
        if z % 2 == 0:
            for i in range(H):
                for j in range(W):
                    work_tree[i][j] += 1

        if z % 2 != 0:
            for i in range(H):
                for j in range(W):
                    work_tree[i][j] += 1

            for x in range(H):
                for y in range(W):
                    if work_tree[x][y] >= 3:
                        if y > 0 and work_tree[x][y-1] < 3:
                            work_tree[x][y-1] = -1
                        if y + 1 < W and work_tree[x][y+1] < 3:
                            work_tree[x][y+1] = -1
                        if x > 0 and work_tree[x-1][y] < 3:
                            work_tree[x-1][y] = -1
                        if x + 1 < H and work_tree[x+1][y] < 3:
                            work_tree[x+1][y] = -1

            for k in range(H):
                for m in range(W):
                    if work_tree[k][m] >= 3 or work_tree[k][m] == -1:
                        work_tree[k][m] = 0

    tree = []
    for i in range(len(work_tree)):
        branch = []
        for j in range(len(work_tree[i])):
            if work_tree[i][j] > 0:
                branch.append('+')
            else:
                branch.append('.')
        branch = ''.join(branch)
        tree.append(branch)
    return tree