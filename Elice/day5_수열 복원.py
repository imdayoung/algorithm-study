import sys


a = []
n = int(sys.stdin.readline())
s = list(map(int, sys.stdin.readline().split()))
s.sort()
checked_sums = [0]

for _ in range(n):
    element = s[1]
    a.append(element)

    new_checked = []
    for checked_sum in checked_sums:
        new_checked.append(checked_sum + element)

    for checked in new_checked:
        s.remove(checked)

    checked_sums += new_checked

print(*a)
