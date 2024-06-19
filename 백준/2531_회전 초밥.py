import sys


# 회전 초밥 벨트에 놓인 접시의 수 N
# 초밥의 가짓수 d
# 연속해서 먹는 접시의 수 k
# 쿠폰 번호 c
N, d, k, c = map(int, sys.stdin.readline().split())

for _ in range(N):
    num = int(sys.stdin.readline())
    