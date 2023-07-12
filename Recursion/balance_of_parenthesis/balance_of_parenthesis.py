def generate_balanced_parentheses(n):
    result = []
    generate("", n, n, result)
    return result

def generate(current, open_count, close_count, result):

    if open_count == 0 and close_count == 0:
        result.append(current)
        return

    if open_count > 0:
        generate(current + "(", open_count - 1, close_count, result)

    if close_count > open_count:
        generate(current + ")", open_count, close_count - 1, result)
