def MadMax(N, Tele):
    Tele.sort()

    impulse = []

    left = sorted(Tele[:N // 2])
    impulse.extend(left)

    right = sorted(Tele[N // 2:], reverse=True)
    impulse.extend(right)

    return impulse

