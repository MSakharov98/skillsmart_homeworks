def find_max(arr, N):
    if not arr:
        return None

    if N == 1:
        return arr[0]

    return max(arr[N - 1], find_max(arr, N - 1))

def find_second_max(arr, N):
    if not arr or N < 2:
        return None

    max_value = find_max(arr, N)
    arr_copy = arr.copy()
    arr_copy.remove(max_value)
    return find_max(arr_copy, N - 1)
