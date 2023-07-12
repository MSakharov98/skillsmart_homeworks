def get_even_indices(lst):
    result = []

    def helper(index=0):
        nonlocal result

        if index >= len(lst):
            return

        if index % 2 == 0 and index != 0:
            result.append(lst[index])

        helper(index + 1)

    helper()

    return result
