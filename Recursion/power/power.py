def power(N, M):

    if M == 0:
        return 1

    if M < 0:
        N = 1 / N
        M = -M

    return N * power(N, M - 1)