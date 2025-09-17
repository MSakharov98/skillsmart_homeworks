def is_palindrom(string: str) -> bool:
    '''
    :param string: string, which is palindrome or not
    :return: bool (True/False) whether if string is palindrom or not
    '''

    if len(string) <= 1:
        return True

    if string[0] != string[-1]:
        return False

    return is_palindrom(string[1:-1])

