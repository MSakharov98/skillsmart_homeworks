def digital_rain(col):
    count_diff = {0: -1}

    count_1 = 0
    count_0 = 0
    max_length = 0
    max_substring = ""

    for right, char in enumerate(col):
        if char == '1':
            count_1 += 1
        else:
            count_0 += 1

        diff = count_1 - count_0

        if diff in count_diff:
            left = count_diff[diff] + 1
            length = right - left + 1
            if length >= max_length:
                max_length = length
                max_substring = col[left:right + 1]
        else:
            count_diff[diff] = right

    return max_substring
