import sys


answer_dna = ""
answer_cnt = 0
N, M = map(int, sys.stdin.readline().split())
dnas = [sys.stdin.readline().rstrip() for _ in range(N)]

for idx in range(M):
    counts = {i:0 for i in range(ord('A'), ord('Z') + 1)}
    for dna in dnas:
        counts[ord(dna[idx])] += 1

    max_count = max(counts.values())
    for key, value in counts.items():
        if value == max_count:
            answer_dna += chr(key)
            answer_cnt += (N - value)
            break

print(answer_dna)
print(answer_cnt)
