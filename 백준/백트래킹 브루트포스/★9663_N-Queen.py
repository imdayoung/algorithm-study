def promising(x):
    for i in range(x):
        if row[x] == row[i]:
            return False
        if abs(row[x] - row[i]) == abs(x - i):
            return False
    return True


def n_queen(x):
    global answer
    if x == N:
        answer += 1
        return
    
    for i in range(N):
        row[x] = i
        if promising(x):
            n_queen(x + 1)


answer = 0
N = int(input())
row = [0] * N
n_queen(0)
print(answer)