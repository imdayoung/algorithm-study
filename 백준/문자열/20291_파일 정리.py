import sys
from collections import Counter
input = sys.stdin.readline

files = []
n = int(input().rstrip())
for _ in range(n):
    name = input().rstrip()
    files.append(name.split('.')[1])
    
files = sorted(Counter(files).most_common())
for i in range(len(files)):
    print(files[i][0], files[i][1])