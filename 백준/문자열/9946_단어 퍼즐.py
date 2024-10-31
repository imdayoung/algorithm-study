import sys


answers = []
while True:
    word = list(map(str, sys.stdin.readline().rstrip()))
    dropped = list(map(str, sys.stdin.readline().rstrip()))

    if (word == ['E', 'N', 'D'] and dropped == ['E', 'N', 'D']):
        break

    word.sort()
    dropped.sort()

    if (word == dropped):
        answers.append("same")
    else:
        answers.append("different")

for i in range(len(answers)):
    print(f"Case {i + 1}: {answers[i]}")
