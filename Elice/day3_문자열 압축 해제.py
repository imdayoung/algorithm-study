import sys


S = sys.stdin.readline().rstrip()
S_len = len(S)

exp = ""

for i in range(S_len):
    char = S[i]
    if char.isdigit():
        if i == S_len - 1:
            exp += char
        elif S[i + 1] == "(":
            exp += char + "*("
        elif S[i + 1] == ")":
            exp += "1"
        else:
            exp += "1+"
    elif char == ")":
        if i == S_len - 1 or S[i + 1] == ")":
            exp += ")"
        else:
            exp += ")+"

answer = eval(exp)
print(answer)
