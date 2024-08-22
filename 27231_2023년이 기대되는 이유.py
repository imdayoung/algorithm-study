# 68%
import sys
sys.stdin = open("input.txt")


def get_new_n(n, n_len, arr, start, count):
    if len(arr) > 0:
        temp = int(n[:arr[0] + 1]) + int(n[arr[-1] + 1:])
        for i in range(len(arr) - 1):
            temp += int(n[arr[i] + 1:arr[i + 1] + 1])
        # print(arr, "->", temp)
        n_new.add(temp)
    
    if count == n_len:
        return
    
    for i in range(start, n_len - 1):
        get_new_n(n, n_len, arr + [i], i + 1, count + 1)


answers = []

T = int(sys.stdin.readline())
for _ in range(T):
    n = int(sys.stdin.readline())
    # print("=================================", n, "=================================")
    n_str = str(n)
    
    n_new = set()
    if len(n_str) == 1:
        n_new.add(n)
    else:
        get_new_n(n_str, len(n_str), [], 0, 0)
    
    # print(n_new)
    
    answer = 0
    for m in range(0, 11):
        temp = 0
        for num in n_str:
            temp += int(num) ** m
        # print("m:", m, ", temp: ", temp)
        if temp in n_new:
            # print(temp, "정답")
            answer += 1
            
    if answer == 11:
        answers.append("Hello, BOJ 2023!")
    else:
        answers.append(answer)

for answer in answers:
    print(answer)
