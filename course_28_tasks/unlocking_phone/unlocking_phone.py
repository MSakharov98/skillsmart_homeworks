def PatternUnlock(N, hits):
    unlock_code = ""
    total_length = 0

    for i in range(1, N):
        distance = 0

        if hits[i] in [2, 9]:
            distance = 1
        else:
            if (hits[i] == 1 and hits[i-1] in [2, 4, 5]):
                distance = 1
            elif (hits[i] == 2 and hits[i-1] in [1, 3, 4, 5, 6]):
                distance = 1
            elif (hits[i] == 3 and hits[i-1] in [2, 5, 6]):
                distance = 1
            elif (hits[i] == 4 and hits[i-1] in [1, 2, 5, 7]):
                distance = 1
            elif (hits[i] == 5 and hits[i-1] in [1, 2, 3, 4, 6, 7, 8, 9]):
                distance = 1
            elif (hits[i] == 6 and hits[i-1] in [2, 3, 5, 8, 9]):
                distance = 1
            elif (hits[i] == 7 and hits[i-1] in [4, 5, 8]):
                distance = 1
            elif (hits[i] == 8 and hits[i-1] in [5, 6, 7, 9]):
                distance = 1
            elif (hits[i] == 9 and hits[i-1] in [6, 8]):
                distance = 1

        total_length += distance

    length_str = str(total_length)

    for char in length_str:
        if char != '0':
            unlock_code += char

    return unlock_code

