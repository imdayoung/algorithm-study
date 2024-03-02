is_prime = [False, False] + [True] * 998
for i in range(2, int(1000 ** 0.5) + 1):
    if is_prime[i]:
        for j in range(i * 2, 1000, i):
            is_prime[j] = False
primes = [i for i in range(2, 1000) if is_prime[i]]
print(primes)

T = int(input())
for tc in range(1, T + 1):
    cnt = 0
    N = int(input())
    M = len(primes)

    for i in range(0, M):
        if primes[i] > N:
            break
        for j in range(i, M):
            if primes[j] > N:
                break
            for k in range(j, M):
                if primes[k] > N:
                    break
                if primes[i] + primes[j] + primes[k] == N:
                    print(primes[i], primes[j], primes[k])
                    cnt += 1
    print(f"#{tc} {cnt}")

# # append, pop 에서 시간 초과 발생 -> 인자로 넘겨주는 방식 사용
# def dfs(start):
#     global cnt
#     if len(temp) == 3:
#         if sum(temp) == N:
#             cnt += 1
#         return
    
#     for i in range(start, M):
#         if primes[i] >= N:
#             break
#         temp.append(primes[i])
#         dfs(i)
#         temp.pop()

# T = int(input())
# for tc in range(1, T + 1):
#     cnt = 0
#     N = int(input())
#     M = len(primes)
#     temp = []
#     dfs(0)
#     print(f"#{tc} {cnt}")

# # 오빠 코드 ㅎㅎ
# def dfs(idx, n, s):
#     global cnt
#     if n == 3:
#         if s == N:
#             cnt += 1
#         return

#     for i in range(idx, len(primes)):
#         if primes[i] >= N:
#             break
#         dfs(i, n + 1, s + primes[i])


# T = int(input())
# for tc in range(1, T + 1):
#     cnt = 0
#     N = int(input())
#     dfs(0, 0, 0)
#     print(f"#{tc} {cnt}")