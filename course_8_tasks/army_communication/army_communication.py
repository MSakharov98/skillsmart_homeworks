def army_communication_matrix(n, matrix):

    prefix_sum = [[0 for _ in range(n)] for _ in range(n)]

    for i in range(n):
        for j in range(n):
            prefix_sum[i][j] = matrix[i][j]
            if i > 0:
                prefix_sum[i][j] += prefix_sum[i-1][j]
            if j > 0:
                prefix_sum[i][j] += prefix_sum[i][j-1]
            if i > 0 and j > 0:
                prefix_sum[i][j] -= prefix_sum[i-1][j-1]

    max_sum = float('-inf')
    result = ""

    for m in range(2, n):
        for i in range(n - m + 1):
            for j in range(n - m + 1):
                total_sum = prefix_sum[i + m - 1][j + m - 1]
                if i > 0:
                    total_sum -= prefix_sum[i - 1][j + m - 1]
                if j > 0:
                    total_sum -= prefix_sum[i + m - 1][j - 1]
                if i > 0 and j > 0:
                    total_sum += prefix_sum[i - 1][j - 1]

                if total_sum > max_sum:
                    max_sum = total_sum
                    result = f"{j} {i} {m}"

    return result

