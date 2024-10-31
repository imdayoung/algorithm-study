import sys


S, C = map(int, sys.stdin.readline().split())
pa = [int(sys.stdin.readline()) for _ in range(S)]

len_pa = 0
start = 1
end = max(pa)

while start <= end:
    mid = (start + end) // 2

    count = 0
    for p in pa:
        count += p // mid
    
    if count < C:
        end = mid - 1
    else:
        len_pa = mid
        start = mid + 1

count = 0

for i in range(S):
    while count < C and pa[i] > 0:
        pa[i] -= len_pa
        count += 1

print(sum(pa))
