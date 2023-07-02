def MisterRobot(N, data):
    if N <= 4:
        return False

    first_element = data[0]
    last_element = data[-1]
    sum_first_last = first_element + last_element

    return sum_first_last % 2 == 0 and first_element < last_element