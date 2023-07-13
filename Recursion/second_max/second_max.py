def find_max(arr, N):
    if not arr:
        return None

    if N == 1:
        return arr[0]

    return max(arr[N - 1], find_max(arr, N - 1))

def find_second_max(arr, N):

    if not arr:
        return None

    return find_max(arr, N - 1)
