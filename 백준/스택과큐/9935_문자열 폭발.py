string = input()
bomb_string = input()
n = len(bomb_string)

stack = []

for char in string:
    stack.append(char)
    if char == bomb_string[-1] and len(stack) >= n and "".join(i for i in stack[len(stack) - n:]) == bomb_string:
            for _ in range(n):
                stack.pop()

if len(stack) == 0:
    print("FRULA")
else:
    print("".join(i for i in stack))


# # 시간 초과
# string = input()
# bomb_string = input()

# bomb_idx = string.find(bomb_string)
# while bomb_idx != -1:
#     string = string.replace(bomb_string, "")
#     bomb_idx = string.find(bomb_string)

# if string == "":
#     print("FRULA")
# else:
#     print(string)