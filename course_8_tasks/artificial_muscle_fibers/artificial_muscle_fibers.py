def artificial_muscle_fibers(arr):
    counter = [0] * 4096

    for num in arr:
        counter[num % 4096] += 1

    count = 0

    for freq in counter:
        if freq > 1:
            count += 1

    return count

