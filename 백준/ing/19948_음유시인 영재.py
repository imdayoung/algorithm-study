import sys


answer = ""

poem = sys.stdin.readline().rstrip()
space_count = int(sys.stdin.readline())
alphabet_counts = list(map(int, sys.stdin.readline().split()))

for i in range(len(poem)):
    word = poem[i]
    ascii_code = ord(word)
    if i > 0 and word == poem[i - 1]:
        continue

    # 대문자
    if 65 <= ascii_code < 91:
        if alphabet_counts[ascii_code - 65] == 0:
            print(-1)
            exit()
        alphabet_counts[ascii_code - 65] -= 1
    # 소문자
    elif 97 <= ascii_code < 123:
        if alphabet_counts[ascii_code - 97] == 0:
            print(-1)
            exit()
        alphabet_counts[ascii_code - 97] -= 1
    else:
        if space_count == 0:
            print(-1)
            exit()
        space_count -= 1

words = poem.split(" ")
print(words)
for i in range(len(words)):
    word = words[i]
    word = word[0].upper()

    answer += word
    if i > 0 and word == words[i - 1][0]:
        continue

    if alphabet_counts[ord(word) - 65] == 0:
        print(-1)
        exit()
    alphabet_counts[ord(word) - 65] -= 1
    
print(answer)
