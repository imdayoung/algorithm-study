n = int(input())
wait = list(map(int, input().split()))
stack = []
target = 1

for i in wait:
    stack.append(i)
    while stack and stack[-1] == target:
        stack.pop()
        target += 1
    if len(stack) > 1 and stack[-2] < stack[-1]:
        print("Sad")
        break

else:
    if stack:
        print("Sad")
    else:
        print("Nice")