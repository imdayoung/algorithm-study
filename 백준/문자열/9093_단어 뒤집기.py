import sys
input = sys.stdin.readline

t = int(input().rstrip())

for _ in range(t):
    string = input().rstrip()
    result = ''
    stack = []

    for i in range(len(string)):
        if string[i] == ' ':
            for _ in range(len(stack)):
                result += stack.pop()
            result += ' '
        else:
            stack.append(string[i])
    result += string.split()[-1][::-1]
    print(result)