current_string = ""
string_changes = []
current_position = -1

def BastShoe(command):
    global current_string, string_changes, current_position

    parts = command.split()
    if len(parts) == 0:
        return current_string

    operation = int(parts[0])

    if operation == 1:
        if len(parts) < 2:
            return current_string

        string_changes = string_changes[:current_position + 1]
        current_string += " ".join(parts[1:])
        string_changes.append(current_string)
        current_position += 1
        return current_string

    if operation == 2:
        if len(parts) < 2:
            return current_string

        string_changes = string_changes[:current_position + 1]
        num_chars = int(parts[1])
        current_string = current_string[:-num_chars]
        string_changes.append(current_string)
        current_position += 1
        return current_string

    if operation == 3:
        if len(parts) < 2:
            return ""

        index = int(parts[1])
        if index < 0 or index >= len(current_string):
            return ""

        return current_string[index]

    if operation == 4:
        if current_position > 0:
            current_position -= 1
            current_string = string_changes[current_position]
        return current_string

    if operation == 5:
        if current_position < len(string_changes) - 1:
            current_position += 1
            current_string = string_changes[current_position]
        return current_string

    return ""