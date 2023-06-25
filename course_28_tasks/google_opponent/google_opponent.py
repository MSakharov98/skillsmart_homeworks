def WordSearch(length, s, subs):
    result = []
    words = s.split()
    lines = []
    current_line = ""

    if len(words) == 1 and len(words[0]) > length:
        current_line = words[0]

        while len(current_line) > length:
            lines.append(current_line[:length])
            current_line = current_line[length:]
        lines.append(current_line)

    else:
        for word in words:
            if len(current_line + word) <= length:
                current_line += word + " "
            else:
                lines.append(current_line.strip())
                current_line = word + " "

        if current_line:
            lines.append(current_line.strip())

    for line in lines:
        words_in_line = line.split()
        found = False

        for word in words_in_line:
            if word == subs:
                found = True
                break

        result.append(int(found))

    return result