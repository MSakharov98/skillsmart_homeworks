def sum_of_numbers(N: int) -> int:

    '''
    параметр N: число, для которого находим сумму цифр
    функция возвращает сумму цифр числа N
    '''

    if N == 0:
        return 0

    if N < 0:
        N = -N

    return sum_of_numbers(N // 10) + (N % 10)


