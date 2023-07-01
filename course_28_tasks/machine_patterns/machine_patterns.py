def LineAnalysis(line):

    if line[0] != '*' or line[-1] != '*':
        return False

    for char in line[1:-1]:
        if char != '.' and char != '*':
            return False

    if line.count('*') != 2:
        return False

    prefix = line.split('*')[0]
    suffix = line.split('*')[-1]
    pattern = line.strip('*')

    if prefix != pattern or suffix != pattern:
        return False

    return True