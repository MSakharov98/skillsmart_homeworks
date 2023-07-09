def TankRush(H1, W1, S1, H2, W2, S2):
    map1 = [list(row) for row in S1.split()]
    map2 = [list(row) for row in S2.split()]

    for i in range(H1 - H2 + 1):
        for j in range(W1 - W2 + 1):
            match = True
            for k in range(H2):
                for l in range(W2):
                    if map1[i + k][j + l] != map2[k][l]:
                        match = False
                        break
                if not match:
                    break
            if match:
                return True

    return False

print(TankRush(3, 4, '125 683 235', 2, 2, '25 32'))