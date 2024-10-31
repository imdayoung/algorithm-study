import sys


N = int(sys.stdin.readline())
N_str = str(N)
n = len(N_str)
s = ""
for i in range(1, N + 1):
    s += str(i)
    
for i in range(len(s) - n + 1):
    if s[i:i + n] == N_str:
        print(i + 1)
        break
