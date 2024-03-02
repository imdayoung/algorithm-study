import sys
input = sys.stdin.readline

N = int(input())
words = []      # 입력받는 단어
selected = []   # 단축키로 지정된 키 저장
answer = []     # 단축키를 지정한 결과

for _ in range(N):
    words.append(input().rstrip())

for word in words:
    
    # 첫 단어의 첫 글자를 단축키로 지정하는 경우
    if word[0].upper() not in selected:
        selected.append(word[0].upper())
        answer.append("[" + word[0] + "]" + word[1:])

    # 두 번째 단어 이상의 첫 글자를 단축키로 지정하는 경우
    else:
        for i in range(1, len(word)):
            if word[i] == " ":
                if word[i + 1].upper() not in selected:
                    selected.append(word[i + 1].upper())
                    answer.append(word[:i + 1] + "[" + word[i + 1] + "]" + word[i + 2:])
                    break
        else:
            # 왼쪽에서부터 알파벳을 보며 단축키를 지정하는 경우
            for i in range(len(word)):
                check = word[i].upper()
                if check != " " and check not in selected:
                    selected.append(check)
                    if i != len(word) - 1:
                        answer.append(word[:i] + "[" + word[i] + "]" + word[i + 1:])
                    else:
                        answer.append(word[:i] + "[" + word[i] + "]")
                    break
            # 단축키를 지정할 수 없는 경우
            else:
                answer.append(word)

for word in answer:
    print(word)