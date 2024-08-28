import sys


answers = []

N, Q = map(int, sys.stdin.readline().split())
soldout = [False for _ in range(N + 1)]

for _ in range(Q):
    x = int(sys.stdin.readline())
    temp = x
    
    result = 0
    walk_through = []

    while temp > 1:
        walk_through.append(temp)
        temp //= 2

    walk_through.sort()
    for ground in walk_through:
        if soldout[ground]:
            result = ground
            break
    
    soldout[x] = True
    answers.append(result)

for answer in answers:
    print(answer)
