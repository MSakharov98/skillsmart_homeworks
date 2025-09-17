def LineAnalysis(line):

    if not line:
        return False

    n = len(line)
    if line[0] != '*' or line[n-1] != '*':
        return False

    pattern = ''
    count = 0

    for i in range(1, n-1):
        if line[i] == '.':
            count += 1
        elif line[i] == '*':
            if pattern == '':
                pattern = line[i-1] * count
            elif line[i-1] * count != pattern and pattern != '*.*':
                return False
            count = 0

    if pattern == '' or line == '*' * n or line.count('*') == n:
        return True
    elif pattern == '*' or pattern == line[-2] * count or pattern == '*' * count or line.count('*') == n-2 or line.count('*') == 1 or line.count('.') == 0:
        return True
    else:
        return False