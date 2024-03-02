import sys
input = sys.stdin.readline


answer = 0

col, row = map(int, input().split())
store_num = int(input())

stores = []
for i in range(1, store_num + 1):
    direction, dist = map(int, input().split())
    if direction == 1:
        stores.append((0, dist))
    elif direction == 2:
        stores.append((row, dist))
    elif direction == 3:
        stores.append((dist, 0))
    else:
        stores.append((dist, col))

direction, dist = map(int, input().split())
if direction == 1:
    cur_x, cur_y = 0, dist
elif direction == 2:
    cur_x, cur_y = row, dist
elif direction == 3:
    cur_x, cur_y = dist, 0
else:
    cur_x, cur_y = dist, col

for store_x, store_y in stores:
    # 같은 행에 있는 경우
    if cur_x == store_x and (cur_x == 0 or cur_x == row):
        answer += abs(cur_y - store_y)
    # 같은 열에 있는 경우
    elif cur_y == store_y and (cur_y == 0 or cur_y == col):
        answer += abs(cur_x - store_x)
    # 반대 행에 있는 경우
    elif cur_x + store_x == row:
        answer += (row + min(cur_y + store_y, col - cur_y + col - store_y))
    # 반대 열에 있는 경우
    elif cur_y + store_y == col:
        answer += (col + min(cur_x + store_x, row - cur_x + row - store_x))
    # 옆 사이드에 있는 경우
    else:
        answer += abs(cur_x - store_x) + abs(cur_y - store_y)

print(answer)