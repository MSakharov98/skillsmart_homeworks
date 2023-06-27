def TheRabbitsFoot(s, encode):
    if encode:
        s = s.replace(' ', '')
        rows = int(len(s)**(1/2) // 1)
        columns = rows + 1

        if rows * columns < len(s):
            rows += 1

        encrypt = []
        while len(s) > columns:
            encrypt.append(list(s[:columns]))
            s = s[columns:]
        else:
            encrypt.append(list(s))

        result = []
        for column in range(columns):
            for row in range(rows):
                if column < len(encrypt[row]):
                    result.append(encrypt[row][column])
            result.append(' ')
        result = ''.join(result).strip()

        return result
    else:
        sequences = s.split()

        symbols = []
        index = 0
        while True:
            for sequence in sequences:
                try:
                    symbol = sequence[index]
                except IndexError:
                    return ''.join(symbols)
                symbols.append(symbol)
            index += 1