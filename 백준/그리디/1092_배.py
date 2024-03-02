import sys
input = sys.stdin.readline


N = int(input())
crain = list(map(int, input().split()))
M = int(input())
boxes = list(map(int, input().split()))

crain.sort(reverse = True)
boxes.sort(reverse = True)

answer = 0
if boxes[0] > crain[0]:
    answer = -1

else:
    while boxes:
        for c in crain:
            if boxes and c < boxes[-1]:
                continue
            for b in boxes:
                if c >= b:
                    boxes.remove(b)
                    break
        answer += 1

print(answer)