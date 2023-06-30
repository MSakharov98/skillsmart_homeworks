def Unmanned(L, N, track):
    total_time = 0
    current_time = 0

    for i in range(N):
        light_time, red_time, green_time = track[i]
        distance = light_time - current_time

        if distance > 0:
            total_time += distance

        if total_time < L:
            cycles = (total_time + red_time) // (red_time + green_time)
            remainder = total_time % (red_time + green_time)

            if remainder < red_time:
                total_time += red_time - remainder

        current_time = light_time

    total_time += L - current_time

    return total_time