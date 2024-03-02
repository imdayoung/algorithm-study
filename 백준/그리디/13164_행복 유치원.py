import sys
input = sys.stdin.readline

N, K = map(int, input().split())
kids = list(map(int, input().split()))
diff = []

# 인접한 학생의 키의 차를 저장하고 정렬함
for i in range(N - 1):
    diff.append(kids[i + 1] - kids[i])
diff.sort()

# N개의 그룹으로 나누면 0임 당연함
# N - 1개의 그룹으로 나누면 차가 가장 최소인 두 명을 합치면 됨 이 값이 diff[0]
# N - 2개의 그룹으로 나눠도 마찬가지로 N - 1개의 그룹으로 나눈 상태에서 차가 최소인 그룹을 또 합침 이 값이 diff[1]이므로 diff[0] + diff[1]
# K번 반복하면 됨
print(sum(diff[:N - K]))