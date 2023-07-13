def find_max(arr, N):
    '''

    :param arr: array, of which we should find max value
    :param N: the length of the array (arr)
    :return: the maximum value of the array (arr) recursively
    '''

    if not arr:
        return None

    if N == 1:
        return arr[0]

    return max(arr[N - 1], find_max(arr, N - 1))

def find_second_max(arr, N):

    '''
    :param arr: array, of which we should find the second maximum value
    :param N: the lenth of the array (arr)
    :return: the second maximum value of the array (arr)
    '''

    if not arr:
        return None

    return find_max(arr, N - 1)
