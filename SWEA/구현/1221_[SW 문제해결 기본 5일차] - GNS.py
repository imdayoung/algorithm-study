nums = {"ZRO":0, "ONE":1, "TWO":2, "THR":3, "FOR":4, "FIV":5, "SIX":6, "SVN":7, "EGT":8, "NIN":9}
nums_2 = {v:k for k, v in nums.items()}

T = int(input())
for _ in range(1, T + 1):
    tc, length = map(str, input().split())
    tc = int(tc[1:])
    length = int(length)

    num = input().split()
    temp = []
    for n in num:
        temp.append(nums[n])
    temp.sort()

    answer = []
    for t in temp:
        answer.append(nums_2[t])

    print(f"#{tc}", end = " ")
    print(*answer)