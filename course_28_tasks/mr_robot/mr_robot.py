def MisterRobot(N, data):
    sorted_data = sorted(data)

    if N < 4 or sorted_data != list(range(1, N+1)):
        return False

    left = 0
    right = 2

    while right < N:
        triplet = sorted_data[left:right+1]
        if triplet[0] > triplet[1] and triplet[1] > triplet[2]:
            return False
        left += 1
        right += 1

    return True



