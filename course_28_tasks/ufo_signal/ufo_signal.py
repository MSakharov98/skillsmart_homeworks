def UFO(N, data, octal):

    if octal:
        system = 8
    else:
        system = 16

    decimal = []

    for number in data:
        decimal.append(int(str(number), system))

    return decimal