import sys
input = sys.stdin.readline

word = input().rstrip()
while word != "end":
    check = 0
    n = len(word)

    # 모음이 포함되어 있는 지 확인
    for i in range(n):
        if word[i] == "a" or word[i] == "e" or word[i] == "i" or word[i] == "o" or word[i] == "u":
            check = 1
            break
    
    # 모음이 3개 연속 또는 자음이 3개 연속인 지 확인
    if check == 1:
        for i in range(n - 2):
            ja, mo = 0, 0
            temp = word[i:i + 3]
            for j in range(3):
                if temp[j] in ["a", "e", "i", "o", "u"]:
                    mo += 1
                else:
                    ja += 1
            if mo == 3 or ja == 3:
                check = 0
                break

    # 같은 글자가 연속으로 두 번 오는 지 확인
    if check == 1:
        for i in range(n - 1):
            temp = word[i:i + 2]
            if temp[0] == temp[1] and temp[0] != "e" and temp[0] != "o":
                check = 0
                break

    if check == 0:
        print(f"<{word}> is not acceptable.")
    else:
        print(f"<{word}> is acceptable.")
    word = input().rstrip()