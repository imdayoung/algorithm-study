import sys
input = sys.stdin.readline

# 주호 개구리의 초기 위치 s, 총 개구리 n마리
s, n = map(int, input().split())
# 개구리들의 좌표
locations = list(map(int, input().split()))
# 점프 거리 k, 1씩 걸을 때마다 소모되는 체력 l
k, l = map(int, input().split())

distance = []

for i in range(len(locations)):
    temp = abs(s - locations[i])
    if k > temp:
        distance.append((i + 1, k + 1))
    elif k == temp:
        distance.append((i + 1, k))
    elif k * 2 > temp:
        distance.append((i + 1, k * 2 - temp))
    else:
        distance.append((i + 1, (temp - k * 2) * l))

distance = sorted(distance, key = lambda x:x[1])
print(distance[0][1], distance[0][0])