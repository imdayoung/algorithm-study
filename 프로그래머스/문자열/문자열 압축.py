def solution(s):
    answer = len(s)
    n = len(s)

    for length in range(1, n // 2 + 1):
        compressed = ""

        check = s[:length]
        cnt = 1

        for i in range(length, n, length):
            if s[i:i + length] == check:
                cnt += 1
            else:
                if cnt > 1:
                    compressed += str(cnt) + check
                else:
                    compressed += check
                check = s[i:i + length]
                cnt = 1

        if cnt > 1:
            compressed += str(cnt) + check
        else:
            compressed += check

        answer = min(answer, len(compressed))

    return answer