import sys


def make_number(num, idx, cnt):
    global answer

    if cnt == N_len:
        if int(num) > N:
            answers.append(int(num))
        return

    for i in range(N_len):
        if i not in idx:
            make_number(num + N_str[i], idx + [i], cnt + 1)


answers = []
N = int(sys.stdin.readline())
N_str = str(N)
N_len = len(N_str)
nums = [num for num in N_str]
make_number("", [], 0)
print(min(answers))
