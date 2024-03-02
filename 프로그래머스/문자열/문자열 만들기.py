def solution(s):
    answer = ''
    for char in s:
        if char == " " or char.isdigit():
            answer += char
        elif (answer != '' and answer[-1] == " ") or answer == '':
            answer += char.upper()
        else:
            answer += char.lower()
    return answer