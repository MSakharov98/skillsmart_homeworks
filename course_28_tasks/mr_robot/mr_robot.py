def MisterRobot(N, data):

    sorted_data = sorted(data)

    if sorted_data == list(range(1, N+1)):
        return True

    for _ in range(N):
        for i in range(N-2):
            triplet = sorted_data[i:i+3]
            triplet = triplet[1:] + [triplet[0]]
            sorted_data[i:i+3] = triplet

            if sorted_data == list(range(1, N+1)):
                return True

    return False
