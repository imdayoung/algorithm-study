from collections import defaultdict

T = int(input())
answers = []
nums = []
for tc in range(1, T + 1):
    A = int(input())
    nums.append(A)

max_nums = max(nums)
prime_num = [False, False] + [True] * max_nums
for i in range(2, int(max_nums ** 0.5) + 1):
    if prime_num[i]:
        for j in range(i * 2, 10 ** 7 + 1, i):
            prime_num[j] = False
    
for num in nums:
    answer = 1

    if prime_num[A] == True:
        answers.append(A)
        
    else:
        nums = defaultdict(int)

        i = 2
        while i <= A:
            if A % i == 0:
                nums[i] += 1
                A //= i
            else:
                i += 1

        for num, cnt in nums.items():
            if cnt % 2 == 1:
                answer *= num

        answers.append(answer)

for i in range(len(answers)):
    print(f"#{i + 1} {answers[i]}")