# 마을을 두 개로 분리
# 각 분리된 마을 안에 집들이 서로 연결되어야 함

# 분리된 두 마을 사이에 있는 길들은 제거
# 분리된 마을 안에서 임의의 두 집 사이에 경로가 항상 존재하게 하면서 길을 없앨 수 있음
# 필요없는 길 모두 없애고 나머지 길의 유지비의 합을 최소로
import sys


N, M = map(int, sys.stdin.readline().split())
for _ in range(M):
    A, B, C = map(int, sys.stdin.readline().split())
    