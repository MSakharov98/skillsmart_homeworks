def SumOfThe(N, data):
    total_sum = sum(data)

    for i in range(N):
        if data[i] == (total_sum - data[i]):
            return data[i]

    return None


