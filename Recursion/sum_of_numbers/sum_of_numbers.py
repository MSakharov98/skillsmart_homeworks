def sum_of_numbers(N: int) -> int:

    '''
    :param N: integer, of which we find the sum of numbers
    function returns sum of numbers of N
    '''

    if N == 0:
        return 0

    if N < 0:
        N = -N

    return sum_of_numbers(N // 10) + (N % 10)
