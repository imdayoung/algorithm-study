import sys


def is_palindrome(s):
    if s == s[::-1]:
        return 0
    return -1


def is_pseudo_palindrome(s):
    i, j = 0, len(s) - 1
    while i < j:
        if s[i] != s[j]:
            if is_palindrome(s[:i] + s[i + 1:]) == 0 or is_palindrome(s[:j] + s[j + 1:]) == 0:
                return 1
            return 2
        i += 1
        j -= 1
        
    return -1


answer = []
T = int(sys.stdin.readline())
strings = [sys.stdin.readline().rstrip() for _ in range(T)]
for string in strings:
    check = is_palindrome(string)
    if check == 0:
        answer.append(check)
    else:
        check = is_pseudo_palindrome(string)
        answer.append(check)

for a in answer:
    print(a)