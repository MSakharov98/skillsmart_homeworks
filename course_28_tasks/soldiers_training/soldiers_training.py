def ConquestCampaign(N, M, L, battalion):
    field = [[0] * M for _ in range(N)]

    for i in range(0, L * 2, 2):
        x = battalion[i] - 1
        y = battalion[i + 1] - 1
        field[x][y] = 1

    day = 1

    while True:
        covered = False

        for i in range(N):
            for j in range(M):
                if field[i][j] == day:
                    if i > 0 and field[i - 1][j] == 0:
                        field[i - 1][j] = day + 1
                        covered = True
                    if i < N - 1 and field[i + 1][j] == 0:
                        field[i + 1][j] = day + 1
                        covered = True
                    if j > 0 and field[i][j - 1] == 0:
                        field[i][j - 1] = day + 1
                        covered = True
                    if j < M - 1 and field[i][j + 1] == 0:
                        field[i][j + 1] = day + 1
                        covered = True

        if not covered:
            break

        day += 1

    return day
