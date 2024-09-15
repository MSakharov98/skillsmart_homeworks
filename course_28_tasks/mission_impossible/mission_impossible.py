from typing import List

def TheRabbitsFoot(s: str, encode: bool) -> str:
    if encode:
        s = s.replace(' ', '')
        rows: int = int(len(s)**(1/2) // 1)
        columns: int = rows + 1

        if rows * columns < len(s):
            rows += 1

        encrypt: List[List[str]] = []
        while len(s) > columns:
            encrypt.append(list(s[:columns]))
            s = s[columns:]
        else:
            encrypt.append(list(s))

        result: List[str] = []
        for column in range(columns):
            for row in range(rows):
                if column < len(encrypt[row]):
                    result.append(encrypt[row][column])
            result.append(' ')
        result = ''.join(result).strip()

        return result
    else:
        sequences: List[str] = s.split()

        symbols: List[str] = []
        index: int = 0
        while True:
            for sequence in sequences:
                try:
                    symbol: str = sequence[index]
                except IndexError:
                    return ''.join(symbols)
                symbols.append(symbol)
            index += 1
