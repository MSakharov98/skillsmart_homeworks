def find_max(arr):
    if not arr:
        return None

    if len(arr) == 1:
        return arr[0]
    else:
        return max(arr[0], find_max(arr[1:]))

def find_second_max(arr):
    if not arr:
        return None

    max_value = find_max(arr)
    arr.remove(max_value)

    return find_max(arr)
