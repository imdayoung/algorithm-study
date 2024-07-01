# K(K > 1)세대 드래곤 커브는 K-1세대 드래곤 커브를 끝 점을 기준으로 90도 시계 방향 회전 시킨 다음, 그것을 끝 점에 붙인 것
import sys


N = int(sys.stdin.readline())
for _ in range(N):
    # d 0: 오른
    # d 1: 위
    # d 2: 왼
    # d 3: 아래
    
    x, y, d, g = map(int, sys.stdin.readline().split())
    