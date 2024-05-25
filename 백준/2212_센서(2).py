import sys


N = int(sys.stdin.readline())
K = int(sys.stdin.readline())
sensors = sorted(list(map(int, sys.stdin.readline().split())))

diff = [sensors[i + 1] - sensors[i] for i in range(N - 1)]
diff.sort()

if N == 1:
    print(0)
    exit()
    
for _ in range(K - 1):
    diff.pop()
    
print(sum(diff))