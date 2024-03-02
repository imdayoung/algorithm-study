tc = int(input())
for i in range(tc):
    n = int(input())    # 문자열의 길이
    s = input().rstrip()
     
    print("#"+str(i + 1), end = " ")
    if n % 2 == 1:
        print("No")
        continue
    if s[:n//2] == s[n//2:]:
        print("Yes")
    else:
        print("No")