def SelectionSortStep(array, i):
    j = i
    for k in range(i, len(array)):
        if array[k] < array[j]:
            j = k
    array[j], array[i] = array[i], array[j]

def BubbleSortStep(array):
    is_sorted = True
    for i in range(1, len(array)):
        if array[i-1] > array[i]:
            array[i-1], array[i] = array[i], array[i-1]
            is_sorted = False
    return is_sorted