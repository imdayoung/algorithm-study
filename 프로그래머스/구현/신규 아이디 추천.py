def solution(new_id):
    answer = ''
    
    # 1단계, 2단계, 3단계
    for char in new_id:
        if char.isalpha():
            answer += char.lower()
        elif (char.isalpha() == False and char in ['-','_']) or (char == '.' and (len(answer) > 0 and answer[-1] != '.' or len(answer) == 0)) or char.isdigit():
            answer += char
    # 4단계
    if len(answer) > 0 and answer[0] == '.':
        answer = answer[1:]
    if len(answer) > 0 and answer[-1] == '.':
        answer = answer[:-1]
    # 5단계
    if len(answer) == 0:
        answer = 'a'
    # 6단계
    if len(answer) >= 16:
        answer = answer[:15]
    if answer[-1] == '.':
        answer = answer[:-1]
    # 7단계
    while len(answer) <= 2:
        answer += answer[-1]
        
    return answer