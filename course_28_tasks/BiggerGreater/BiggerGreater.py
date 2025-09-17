def BiggerGreater(input):
    input = list(input)

    index_i = -1
    index_j = -1

    for i in range(len(input) - 2, -1, -1):
        if input[i] < input[i + 1]:
            index_i = i
            break

    if index_i == -1:
        return ''

    for j in range(len(input) - 1, index_i, -1):
        if input[j] > input[index_i]:
            index_j = j
            break

    input[index_i], input[index_j] = input[index_j], input[index_i]

    input[index_i + 1:] = sorted(input[index_i + 1:])

    return ''.join(input)