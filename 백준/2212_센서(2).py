import sys


N = int(sys.stdin.readline())
K = int(sys.stdin.readline())
sensors = list(set(map(int, sys.stdin.readline().split())))
sensors.sort()
print("sensors: ", sensors)

# diff = []
# for i in range(N - 2):
#     print(sensors[i + 1], sensors[i], sensors[i + 1] - sensors[i])
#     diff.append(sensors[i + 1] - sensors[i])

# print("diff:", diff)