def solution(survey, choices):
    answer = ''
    result = {"R":0, "T":0, "C":0, "F":0, "J":0, "M":0, "A":0, "N":0}
    
    for i in range(len(survey)):
        if (survey[i] == "RT" and choices[i] < 4) or (survey[i] == "TR" and choices[i] > 4):
            result["R"] += abs(4 - choices[i])
        elif (survey[i] == "TR" and choices[i] < 4) or (survey[i] == "RT" and choices[i] > 4):
            result["T"] += abs(4 - choices[i])
        elif (survey[i] == "FC" and choices[i] < 4) or (survey[i] == "CF" and choices[i] > 4):
            result["F"] += abs(4 - choices[i])
        elif (survey[i] == "CF" and choices[i] < 4) or (survey[i] == "FC" and choices[i] > 4):
            result["C"] += abs(4 - choices[i])
        elif (survey[i] == "MJ" and choices[i] < 4) or (survey[i] == "JM" and choices[i] > 4):
            result["M"] += abs(4 - choices[i])
        elif (survey[i] == "JM" and choices[i] < 4) or (survey[i] == "MJ" and choices[i] > 4):
            result["J"] += abs(4 - choices[i])
        elif (survey[i] == "AN" and choices[i] < 4) or (survey[i] == "NA" and choices[i] > 4):
            result["A"] += abs(4 - choices[i])
        else:
            result["N"] += abs(4 - choices[i])
            
    if result["R"] >= result["T"]: answer += "R"
    else: answer += "T"
    if result["C"] >= result["F"]: answer += "C"
    else: answer += "F"
    if result["J"] >= result["M"]: answer += "J"
    else: answer += "M"
    if result["A"] >= result["N"]: answer += "A"
    else: answer += "N"
    return answer