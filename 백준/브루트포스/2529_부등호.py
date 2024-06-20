import sys


def find_min(now, cnt, nums):
    global answer_min
    if answer_min != "":
        return
    
    if cnt == k:
        answer_min = ''.join(str(num) for num in nums)
        return

    if signs[cnt] == "<":
        if now == 9:
            return
        for i in range(now + 1, 10):
            if i not in nums:
                find_min(i, cnt + 1, nums + [i])
    else:
        if now == 0:
            return
        for i in range(now):
            if i not in nums:
                find_min(i, cnt + 1, nums + [i])


def find_max(now, cnt, nums):
    global answer_max
    if answer_max != "":
        return
    
    if cnt == k:
        answer_max = ''.join(str(num) for num in nums)
        return

    if signs[cnt] == "<":
        if now == 9:
            return
        for i in range(9, now, -1):
            if i not in nums:
                find_max(i, cnt + 1, nums + [i])
    else:
        if now == 0:
            return
        for i in range(now - 1, -1, -1):
            if i not in nums:
                find_max(i, cnt + 1, nums + [i])


k = int(sys.stdin.readline())
signs = list(map(str, sys.stdin.readline().split()))
answer_min = ""
answer_max = ""

for i in range(10):
    find_min(i, 0, [i])
    if answer_min != "":
        break
for i in range(9, -1, -1):
    find_max(i, 0, [i])
    if answer_max != "":
        break

print(answer_max)
print(answer_min)