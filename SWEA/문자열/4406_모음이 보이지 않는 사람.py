T = int(input())
for tc in range(1, T + 1):
    answer = ""
    word = input()
    for char in word:
        if char not in ["a", "e", "i", "o", "u"]:
            answer += char
    print(f"#{tc} {answer}")