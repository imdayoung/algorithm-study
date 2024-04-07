import sys


# 모든 칸의 높이가 모드 같은지 판별
def is_equal_height(bridge):
    height = bridge[0]
    for i in range(1, N):
        if bridge[i] != height:
            return False
    return True


# 경사로를 놓아서 길을 지나갈 수 있는지 판별
def is_makable(bridge):
    # 경사로를 설치했는지 저장
    constructed = [False for _ in range(N)]
    # 같은 높이의 길이 몇개가 연속되어있는지 저장
    continuous = 1

    i = 0
    while i < N - 1:
        # 연속된 길의 높이가 같은 경우
        if bridge[i] == bridge[i + 1]:
            continuous += 1
            i += 1

        # 현재 길의 높이가 다음 길의 높이보다 높은 경우
        # 다음 길의 높이가 L개 이상 연속되어 있어야 함
        elif bridge[i] == bridge[i + 1] + 1:
            continuous = 0
            new_i = i
            
            for j in range(i + 1, N):
                if bridge[j] == bridge[i + 1]:
                    continuous += 1
                    new_i += 1
                else:
                    break

            if continuous < L:
                return False
            
            for j in range(i + 1, i + 1 + L):
                if constructed[j]:
                    return False
                constructed[j] = True

            i = new_i

        # 현재 길의 높이가 다음 길의 높이보다 낮은 경우
        # 현재 길의 높이에 해당하는 길에 경사로를 설치할 수 있어야 함
        elif bridge[i] == bridge[i + 1] - 1:
            if continuous < L:
                return False
            else:
                for j in range(i, i - L, -1):
                    if constructed[j]:
                        return False
                    constructed[j] = True
                i += 1

        # 높이 차가 2 이상인 경우
        else:
            return False

    return True


answer = 0
N, L = map(int, sys.stdin.readline().split())
graph = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

for i in range(N):
    if is_equal_height(graph[i]):
        answer += 1
    elif is_makable(graph[i]):
        answer += 1

graph_rev = [[a[i] for a in graph] for i in range(N)]
for i in range(N):
    if is_equal_height(graph_rev[i]):
        answer += 1
    elif is_makable(graph_rev[i]):
        answer += 1

print(answer)