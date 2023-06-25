def WordSearch(length, s, subs):
    result = []
    words = s.split()
    lines = []
    current_line = ""

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