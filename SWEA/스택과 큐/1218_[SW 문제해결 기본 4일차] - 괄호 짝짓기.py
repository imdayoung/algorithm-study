T = 10
for tc in range(1, T + 1):
    answer = 0
    stack = []

    N = int(input())
    bracket = list(map(str, input()))

    for b in bracket:
        if b == "(" or b == "[" or b == "{" or b == "<":
            stack.append(b)

        elif b == ")":
            if stack and stack[-1] == "(":
                stack.pop()
            else:
                break

        elif b == "]":
            if stack and stack[-1] == "[":
                stack.pop()
            else:
                break

        elif b == "}":
            if stack and stack[-1] == "{":
                stack.pop()
            else:
                break

        elif b == ">":
            if stack and stack[-1] == "<":
                stack.pop()
            else:
                break

    if not stack:
        answer = 1
    print(f"#{tc} {answer}")