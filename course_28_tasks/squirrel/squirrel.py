def squirrel(N):
    factorial = 1
    for i in range(2, N + 1):
        factorial *= i

    first_digit = int(str(factorial)[0])
    return first_digit
