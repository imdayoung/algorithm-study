import sys


def get_probable_list(visited, cnt, num):
    if cnt == 3:
        probables.append(num)
        return
    
    for i in range(1, 9 + 1):
        if not visited[i]:
            visited[i] = True
            get_probable_list(visited, cnt + 1, num + str(i))
            visited[i] = False


answer = 0

probables = []
get_probable_list([False for _ in range(10)], 0, "")

N = int(sys.stdin.readline())
for _ in range(N):
    prob = []
    number, strike, ball = map(int, sys.stdin.readline().split())
    number = str(number)
    
    for probable in probables:
        strike_count = 0
        ball_count = 0

        for i in range(3):
            if number[i] == probable[i]:
                strike_count += 1
            elif number[i] in probable:
                ball_count += 1

        if strike_count == strike and ball_count == ball:
            prob.append(probable)

    probables = prob

print(len(probables))
