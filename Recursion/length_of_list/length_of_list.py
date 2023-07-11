def length_of_list(l: list) -> int:
    '''
    :param l: is a list, which length we should find
    :return: integer, that is the length of the list l
    '''

    if not l:
        return 0

    l.pop(0)

    return 1 + length_of_list(l)
