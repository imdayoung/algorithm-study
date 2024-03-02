import sys


def my_round(val, digits):
    return round(val + 10 ** (-len(str(val)) - 1), digits)


size = 0
N = int(sys.stdin.readline())

dots = []
for _ in range(N):
    x, y = map(int, sys.stdin.readline().split())
    dots.append((x, y))

temp1, temp2 = 0, 0
x1 = dots[0][0]
y1 = dots[0][1]
for i in range(1, len(dots) - 1):
    x2 = dots[i][0]
    y2 = dots[i][1]
    x3 = dots[i + 1][0]
    y3 = dots[i + 1][1]
    temp1 += (x1 * y2 + x2 * y3 + x3 * y1)
    temp2 += (y1 * x2 + y2 * x3 + y3 * x1)

print(my_round(abs(temp1 - temp2) * 0.5, 1))

# import sys


# def my_round(val, digits):
#     return round(val + 10 ** (-len(str(val)) - 1), digits)


# size = 0
# N = int(sys.stdin.readline())

# dots = []
# for _ in range(N):
#     x, y = map(int, sys.stdin.readline().split())
#     dots.append((x, y))

# x1 = dots[0][0]
# y1 = dots[0][1]
# for i in range(1, len(dots) - 1):
#     x2 = dots[i][0]
#     y2 = dots[i][1]
#     x3 = dots[i + 1][0]
#     y3 = dots[i + 1][1]
#     size += abs((x1 * y2 + x2 * y3 + x3 * y1) - (y1 * x2 + y2 * x3 + y3 * x1)) * 0.5

# print(my_round(size, 1))

# for i in range(len(dots) - 2):
#     x1 = dots[i][0]
#     y1 = dots[i][1]
#     x2 = dots[i + 1][0]
#     y2 = dots[i + 1][1]
#     x3 = dots[i + 2][0]
#     y3 = dots[i + 2][1]
#     size += abs((x1 * y2 + x2 * y3 + x3 * y1) - (y1 * x2 + y2 * x3 + y3 * x1)) * 0.5

# print(my_round(size, 1))