def find_second_max_recursive(x, i, first_max, second_max):
    if i >= len(x):
        return second_max

    if x[i] >= first_max:
        second_max = first_max
        first_max = x[i]
    elif x[i] > second_max:
        second_max = x[i]

    return find_second_max_recursive(x, i + 1, first_max, second_max)


def find_second_max(x):
    if not x:
        return None

    first_max = x[0]
    second_max = x[1]

    second_max = find_second_max_recursive(x, 0, first_max, second_max)

    return second_max

