def odometer(oksana):
    total_distance = 0
    prev_time = 0

    for i in range(0, len(oksana), 2):
        speed = oksana[i]
        time = oksana[i + 1]
        distance = speed * (time - prev_time)
        total_distance += distance
        prev_time = time

    return total_distance
