def BigMinus(s1, s2):

    s1 = s1.lstrip('0')
    s2 = s2.lstrip('0')

    max_length = max(len(s1), len(s2))
    s1 = s1.zfill(max_length)
    s2 = s2.zfill(max_length)

    if s1 < s2:
        s1, s2 = s2, s1

    result = ''
    borrow = 0

    for i in range(max_length - 1, -1, -1):
        digit1 = int(s1[i])
        digit2 = int(s2[i])

        diff = digit1 - digit2 - borrow

        if diff < 0:
            diff += 10
            borrow = 1
        else:
            borrow = 0

        result = str(diff) + result

    result = result.lstrip('0')

    if not result:
        result = '0'

    return result