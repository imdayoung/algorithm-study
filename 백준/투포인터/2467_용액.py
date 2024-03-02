N = int(input())
liquids = list(map(int, input().split()))

answer_left, answer_right = liquids[-2], liquids[-1]
nearest = abs(liquids[-1] + liquids[-2])

start, end = 0, N - 1
while start < end:
    temp = liquids[start] + liquids[end]
    if temp > 0:
        if abs(temp) < nearest:
            nearest = abs(temp)
            answer_left, answer_right = liquids[start], liquids[end]
        end -= 1

    elif temp < 0:
        if abs(temp) < nearest:
            nearest = abs(temp)
            answer_left, answer_right = liquids[start], liquids[end]
        start += 1

    else:
        answer_left, answer_right = liquids[start], liquids[end]
        break

print(answer_left, answer_right)