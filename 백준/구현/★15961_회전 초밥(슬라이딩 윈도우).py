# https://wooono.tistory.com/655

from collections import  defaultdict
import sys
input = sys.stdin.readline

# N 회전 초밥 벨트에 놓인 접시의 수
# d 초밥의 가짓수
# k 연속해서 먹는 접시의 수
# c 쿠폰 번호
N, d, k, c = map(int, input().split())

# 초밥 접시 상황
sushis = [int(input()) for _ in range(N)]

# 구간 내의 접시 종류별 개수
plates = defaultdict(int)

# 구간 내에 쿠폰이 항상 포함되어 있다고 가정
plates[c] = 1

# 첫 시작 구간의 접시 종류별 개수 저장
left, right = 0, k - 1
for i in range(right + 1):
    plates[sushis[i]] += 1

# 구간 내의 최대 접시 종류 개수 초기화
answer = -int(1e9)

# 슬라이딩 윈도우 진행
while left < N:
    # 현재 구간 내의 접시 종류 개수와 최대 접시 종류 개수를 비교
    result = max(len(plates), result)

    # 윈도우를 오른쪽으로 한 칸씩 이동하기 위한 작업 진행

    # 현재 구간 내의 가장 왼쪽 접시를 제거
    plates[sushis[left]] -= 1
    # 이제 해당 종류의 접시가 남아있지 않다면, 딕셔너리에서 제거
    if (plates[sushis[left]] == 0):
        del plates[sushis[left]]
    # 왼쪽 인덱스를 오른쪽으로 한 칸 이동
    left += 1

    # 오른쪽 인덱스를 오른쪽으로 한 칸 이동
    right += 1
    # 현재 구간 내의 가장 오른쪽 접시를 추가
    plates[sushis[right % N]] += 1

print(answer)