def TRC_sort(trc):

    count = [0] * 3

    for num in trc:
        count[num] += 1

    sorted_trc = []

    for i in range(3):
        sorted_trc.extend([i] * count[i])

    return sorted_trc
