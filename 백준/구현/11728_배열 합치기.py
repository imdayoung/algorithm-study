N, M = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
res = []

a, b = 0, 0
while a < N or b < M:
    if  a == N:
        res.append(B[b])
        b += 1
    elif b == M:
        res.append(A[a])
        a += 1
    else:
        if A[a] < B[b]:
            res.append(A[a])
            a += 1
        else:
            res.append(B[b])
            b += 1

print(*res)