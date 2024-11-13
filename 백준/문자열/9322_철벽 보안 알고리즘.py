import sys


answers = []
T = int(sys.stdin.readline())
for _ in range(T):
    original = ""

    n = int(sys.stdin.readline())
    first_key = list(map(str, sys.stdin.readline().rstrip().split()))
    second_key = list(map(str, sys.stdin.readline().rstrip().split()))
    secret = list(map(str, sys.stdin.readline().rstrip().split()))

    for i in range(n):
        s = first_key[i]
        a = second_key.index(s)
        print(second_key.index(first_key[i]))
        original += secret[a] + " "

    answers.append(original.rstrip())

for answer in answers:
    print(answer)
