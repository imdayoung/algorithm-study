import sys
input = sys.stdin.readline

mk = input().rstrip()
max_mk = ""
min_mk = ""

cnt_m = 0
for char in mk:
    if char == "M":
        cnt_m += 1

    elif char == "K":
        if cnt_m > 0:
            max_mk += str(5 * (10 ** (cnt_m)))
            min_mk += str(10 ** (cnt_m - 1)) + "5"
            cnt_m = 0

        else:
            max_mk += "5"
            min_mk += "5"

if cnt_m > 0:
    max_mk += "1" * cnt_m
    min_mk += str(10 ** (cnt_m - 1))

print(max_mk)
print(min_mk)