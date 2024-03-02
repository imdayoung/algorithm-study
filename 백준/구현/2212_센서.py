import sys


N = int(sys.stdin.readline())
K = int(sys.stdin.readline())
sensors = sorted(list(map(int, sys.stdin.readline().split())))

diff = []
for i in range(N - 1):
    temp = sensors[i + 1] - sensors[i]
    if temp != 0:
        diff.append(temp)

if len(diff) == 0:
    print(0)
    exit()

diff.sort()
for _ in range(K - 1):
    diff.pop()

print(sum(diff))


# import sys


# N = int(sys.stdin.readline())
# K = int(sys.stdin.readline())
# sensors = sorted(list(map(int, sys.stdin.readline().split())))

# diff = []
# for i in range(N - 1):
#     temp = sensors[i + 1] - sensors[i]
#     if temp != 0:
#         diff.append(temp)

# if len(diff) == 0:
#     print(0)
#     exit()

# for _ in range(K - 1):
#     max_value = max(diff)
#     for i in range(len(diff)):
#         if diff[i] == max_value:
#             diff[i] = 0
#             break

# print(sum(diff))