from collections import deque

T = int(input())
for tc in range(1, T + 1):
    answer = ""

    string_1 = deque(list(map(str, input())))
    string_2 = deque(list(map(str, input())))
    string_3 = deque(list(map(str, input())))
    string_4 = deque(list(map(str, input())))
    string_5 = deque(list(map(str, input())))

    while string_1 or string_2 or string_3 or string_4 or string_5:
        if string_1:
            answer += string_1.popleft()
        if string_2:
            answer += string_2.popleft()
        if string_3:
            answer += string_3.popleft()
        if string_4:
            answer += string_4.popleft()
        if string_5:
            answer += string_5.popleft()
        
    print(f"#{tc} {answer}")