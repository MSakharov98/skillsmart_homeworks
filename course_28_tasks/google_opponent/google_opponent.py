def WordSearch(length, s, subs):
    result = []
    words = s.split()

    if len(words) == 1 and len(words[0]) > length:
        # Обработка случая, когда строка без пробелов превышает длину length
        line = words[0]
        result.extend(int(subs == line[i:i + length]) for i in range(0, len(line), length))

    else:
        # Разбиение строки на подстроки длиной length
        lines = []
        line = ""

        for word in words:
            if len(line) + len(word) <= length:
                line += word + " "
            else:
                lines.append(line.strip())
                line = word + " "

        if line:
            lines.append(line.strip())

        # Поиск вхождений subs в каждую подстроку
        result = [int(subs in line.split()) for line in lines]

    return result
