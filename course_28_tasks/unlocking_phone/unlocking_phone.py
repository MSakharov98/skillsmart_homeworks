def PatternUnlock(N, hits):
    diagonal_points = [2, 4, 6, 8]
    length = 0
    previous_point = hits[0]

    for i in range(1, N):
        current_point = hits[i]

        if (previous_point in diagonal_points and current_point in diagonal_points) or \
                (previous_point not in diagonal_points and current_point not in diagonal_points):
            length += 1
        else:
            length += 1.41421

        previous_point = current_point

    rounded_length = round(length, 5)

    result = str(rounded_length).replace(".", "")

    return result
