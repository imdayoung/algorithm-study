cries = [0 for _ in range(5)]
answer = 0

for char in input():
    if char == 'q':
        cries[0] += 1
        if cries[4]:
            cries[4] -= 1
        else:
            answer += 1
    elif char == 'u' and cries[0]:
        cries[0] -= 1
        cries[1] += 1
    elif char == 'a' and cries[1]:
        cries[1] -= 1
        cries[2] += 1
    elif char == 'c' and cries[2]:
        cries[2] -= 1
        cries[3] += 1
    elif char == 'k' and cries[3]:
        cries[3] -= 1
        cries[4] += 1
    else:
        cries[0] = 1
        break
print(answer if sum(cries[:4]) == 0 else -1)