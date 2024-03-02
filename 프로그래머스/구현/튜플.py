def solution(s):
    answer = []
    
    # 튜플을 표현하는 집합을 구분
    tuples = []
    tuple_temp = []
    num_temp = ""
    for i in range(len(s)):
        char = s[i]
        if char == "}" or char == ",":
            if num_temp.isdigit():
                tuple_temp.append(int(num_temp))
                num_temp = ""
            if char == "}":
                tuples.append(tuple_temp)
                tuple_temp = []
        elif char.isdigit():
            num_temp += char
    tuples.sort(key = len)
    
    for i in range(1, len(tuples)):
        for j in tuples[i]:
            if j not in answer:
                answer.append(j)
                break
    
    return answer