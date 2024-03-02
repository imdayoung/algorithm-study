from collections import deque

for _ in range(10):
    tc = int(input())
    nums = deque(list(map(int, input().split())))

    while True:
        for i in range(1, 6):
            temp = nums.popleft() - i
            if temp <= 0:
                nums.append(0)
                break
            else:
                nums.append(temp)
        if nums[-1] == 0:
            break

    print(f'#{tc}', *nums)