max_value = 1000000
is_prime = [False, False] + [True] * max_value

for i in range(2, int(max_value * 0.5) + 1):
    if is_prime[i]:
        for j in range(i * 2, max_value + 1, i):
            is_prime[j] = False

M, N = map(int, input().split())
for i in range(M, N + 1):
    if is_prime[i]:
        print(i)