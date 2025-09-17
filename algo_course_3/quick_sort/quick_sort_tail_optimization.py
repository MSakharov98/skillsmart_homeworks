def ArrayChunk(array, left, right):
    i = left
    j = right
    N = (i + j + 1) // 2
    while True:
        if array[i] < array[N]:
            i += 1
        if array[j] > array[N]:
            j -= 1
        if i == j-1 and array[i] > array[j]:
            array[i], array[j] = array[j], array[i]
            return ArrayChunk(array, left, right)
        if i == j or (i == j-1 and array[i] < array[j]):
            return N
        if array[i] >= array[N] and array[j] <= array[N]:
            array[i], array[j] = array[j], array[i]
            if i == N:
                N = j
            elif j == N:
                N = i

def QuickSortTailOptimization(array, left, right):
    while left < right:
        middle = ArrayChunk(array, left, right)
        QuickSortTailOptimization(array, left, middle-1)
        left = middle + 1