from collections import deque


N = int(input())
odds = ["1", "3", "5", "7", "9"]
queue = deque([2, 3, 5, 7])
repeat = len(queue)

for _ in range(N - 1):
    for _ in range(repeat):
        x = queue.popleft()
        for post in odds:
            temp = int(str(x) + post)
            for i in range(2, int(temp ** 0.5) + 1):
                if temp % i == 0:
                    break
            else:
                queue.append(temp)
    repeat = len(queue)

for num in queue:
    print(num)