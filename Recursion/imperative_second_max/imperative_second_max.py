def find_second_max(x):

    if not x:
        return []

    first_max = -1e9
    second_max = -1e9

    for i in range(len(x)):
        if x[i] >= first_max:
            second_max = first_max
            first_max = x[i]
        elif x[i] > second_max:
            second_max = x[i]

    return second_max
