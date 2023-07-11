def only_even_values(l: list) -> list:
    '''
    :param l: list, where we check even values
    :return: list with only even values of l
    '''

    even_values = []

    if not l:
        return even_values

    if l[0] % 2 == 0:
        even_values.append(l[0])

    even_values.extend(only_even_values(l[1:]))

    return even_values







