def even_indices(lst, index=None):

    if index is None:
        index = 0

    if index >= len(lst):
        return []

    result = []

    if index % 2 == 0 and index != 0:
        result.append(lst[index])

    return result + even_indices(lst, index + 1)


