def ArrayChunk(array):
    middle_index = len(array) // 2
    left_index = 0
    right_index = len(array) - 1
    while True:
        if array[left_index] < array[middle_index]:
            left_index += 1
        if array[right_index] > array[middle_index]:
            right_index -= 1
        if left_index == right_index - 1 and array[left_index] > array[right_index]:
            array[left_index], array[right_index] = array[right_index], array[left_index]
            return ArrayChunk(array)
        if left_index == right_index or (left_index == right_index - 1 and array[left_index] < array[right_index]):
            return middle_index
        if array[left_index] >= array[middle_index] and array[right_index] <= array[middle_index]:
            array[left_index], array[right_index] = array[right_index], array[left_index]
            if left_index == middle_index:
                middle_index = right_index
            elif right_index == middle_index:
                middle_index = left_index
