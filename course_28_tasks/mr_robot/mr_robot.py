def MisterRobot(N, data):

    if N < 4 or set(data) != set(range(1, N + 1)):
        return False

    for i in range(N - 2):
        triplet = data[i:i+3]
        if triplet[0] > triplet[1] and triplet[1] > triplet[2]:
            return False

    return True