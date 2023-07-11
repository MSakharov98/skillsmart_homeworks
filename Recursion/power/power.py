def power(N, M):
    if M == 0:
        return 1
    elif M < 0:
        return 1 / power(N, -M)
    else:
        return N * power(N, M - 1)