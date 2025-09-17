def PatternUnlock(N, hits):
    straight = 1
    diagonal = 2 ** (1 / 2)
    keyboard = [[6, 1, 9], [5, 2, 8], [4, 3, 7]]
    sequence = []

    for hit in range(len(hits)):
        if hits[hit] == hits[-1]:
            break
        for row in range(len(keyboard)):
            for column in range(len(keyboard[row])):
                if hits[hit] == keyboard[row][column]:

                    if 0 <= row - 1 <= 2 and keyboard[row - 1][column] == hits[hit + 1]:
                        sequence.append(straight)
                    if 0 <= row + 1 <= 2 and keyboard[row + 1][column] == hits[hit + 1]:
                        sequence.append(straight)
                    if 0 <= column - 1 <= 2 and keyboard[row][column - 1] == hits[hit + 1]:
                        sequence.append(straight)
                    if 0 <= column + 1 <= 2 and keyboard[row][column + 1] == hits[hit + 1]:
                        sequence.append(straight)

                    if 0 <= row + 1 <= 2 and 0 <= column + 1 <= 2 and keyboard[row + 1][column + 1] == hits[hit + 1]:
                        sequence.append(diagonal)
                    if 0 <= row + 1 <= 2 and 0 <= column - 1 <= 2 and keyboard[row + 1][column - 1] == hits[hit + 1]:
                        sequence.append(diagonal)
                    if 0 <= row - 1 <= 2 and 0 <= column - 1 <= 2 and keyboard[row - 1][column - 1] == hits[hit + 1]:
                        sequence.append(diagonal)
                    if 0 <= row - 1 <= 2 and 0 <= column + 1 <= 2 and keyboard[row - 1][column + 1] == hits[hit + 1]:
                        sequence.append(diagonal)

    summ = sum(sequence)

    summ = float('{:.5f}'.format(summ))

    summ = str(summ)

    result_without_zero = summ.replace('0', '')
    result = result_without_zero.replace('.', '')

    return result