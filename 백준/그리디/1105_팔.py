import sys


answer = 0

L, R = map(str, sys.stdin.readline().split())
len_L, len_R = len(L), len(R)

if len_L != len_R:
    answer = 0
else:
    for i in range(len_L):
        if L[i] == R[i] == '8':
            answer += 1
        elif L[i] != R[i]:
            break
    
print(answer)