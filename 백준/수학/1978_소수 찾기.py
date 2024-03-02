n = int(input())
nums = list(map(int, input().split()))

temp = [False, False] + [True] * (1000 - 1)
answer = 0

for i in range(2, int(1000 ** 0.5) + 1):
    if temp[i]:
        for j in range(i * 2, 1000 + 1, i):
            temp[j] = False

for num in nums:
    if temp[num]:
        answer += 1
        
print(answer)