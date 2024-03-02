import sys
import heapq
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    min_hq, max_hq = [], []
    nums = {}

    k = int(input())
    for _ in range(k):
        command = input().rstrip()
        cmd = command.split()[0]
        val = int(command.split()[1])

        if cmd == "I":
            heapq.heappush(min_hq, val)
            heapq.heappush(max_hq, -val)
            if val in nums:
                nums[val] += 1
            else:
                nums[val] = 1
        else:
            if val == -1:
                while min_hq:
                    temp = heapq.heappop(min_hq)
                    if nums[temp] > 0:
                        nums[temp] -= 1
                        break
            else:
                while max_hq:
                    temp = -heapq.heappop(max_hq)
                    if nums[temp] > 0:
                        nums[temp] -= 1
                        break

    result = []
    for key, val in nums.items():
        if val > 0:
            result.append(key)
    if result:
        print(max(result), min(result))
    else:
        print("EMPTY")