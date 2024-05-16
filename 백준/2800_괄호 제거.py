import sys


def backtracking(arr, start):
    if arr != []:
        get_new_exp(arr)

    if len(arr) == m:
        return
    
    for i in range(start, m):
        backtracking(arr + [i], i + 1)


def get_new_exp(arr):
    global answers
    new_exp = list(exp)

    for i in arr:
        new_exp[brackets[i][0]] = ""
        new_exp[brackets[i][1]] = ""

    answers.append(''.join(i for i in (new_exp)))


answers = []

exp = sys.stdin.readline().rstrip()
n = len(exp)

brackets = []
stack = []
for i in range(n):
    if exp[i] == "(":
        stack.append(i)
    elif exp[i] == ")":
        idx_start = stack.pop()
        brackets.append((idx_start, i))

m = len(brackets)
backtracking([], 0)

answers = list(set(answers))
answers.sort()
for answer in answers:
    print(answer)