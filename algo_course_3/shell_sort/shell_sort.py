def InsertionSortStep(array, step, i):
    for s in range(i + step, len(array), step):
        for j in range(s, i + step - 1, -step):
            if array[j] < array[j - step]:
                array[j], array[j - step] = array[j - step], array[j]


def KnuthSequence(array_size, k_seq=None, i=1):
    if k_seq is None:
        k_seq = []
    if not array_size:
        return [1]
    if array_size >= i:
        KnuthSequence(array_size, k_seq, 3 * i + 1)
        k_seq.append(i)
    return k_seq
