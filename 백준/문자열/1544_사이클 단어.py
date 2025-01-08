import sys


N = int(sys.stdin.readline())
words = []
for _ in range(N):
    cur = sys.stdin.readline().rstrip()
    is_same = False
    for prev in words:
        if len(prev) == len(cur):
            for i in range(len(cur)):
                if prev[i] == cur[0]:
                    if prev[i:] + prev[:i] == cur:
                        is_same = True
                        break
        if is_same:
            break
    if not is_same:            
        words.append(cur)
    
print(len(words))
