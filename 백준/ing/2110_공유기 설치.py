import sys


N, C = map(int, sys.stdin.readline().split())
router = [int(sys.stdin.readline()) for _ in range(N)]
router.sort()
print(router)

start = 1
end = router[-1] - router[0]

while start <= end:
    mid = (start + end) // 2
    