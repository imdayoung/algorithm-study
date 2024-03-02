def solution(info, query):
    query_dict = {}
    for i in range(len(query)):
        conditions = query[i].split()
        lang, apply, career, food, score = conditions[0], conditions[2], conditions[4], conditions[6], int(conditions[7])
        query_dict[i] = [score, lang, apply, career, food]
    query_dict = sorted(query_dict.values(), key = lambda x : x[0])
    print(query_dict)

    for applier in info:
        applier = applier.split()
        applier_lang, applier_apply, applier_career, applier_food, applier_score = applier[0], applier[1], applier[2], applier[3], int(applier[4])
        print(applier_lang, applier_apply, applier_career, applier_food, applier_score)

    answer = []
    return answer

# # 당연하게 효율성 테스트 실패
# def solution(info, query):
#     answer = []

#     for q in query:
#         meet = 0
#         conditions = q.split()
#         lang, apply, career, food, score = conditions[0], conditions[2], conditions[4], conditions[6], int(conditions[7])

#         for applier in info:
#             applier = applier.split()
#             applier_lang, applier_apply, applier_career, applier_food, applier_score = applier[0], applier[1], applier[2], applier[3], int(applier[4])
            
#             if lang == applier_lang or lang == "-":
#                 if apply == applier_apply or apply == "-":
#                     if career == applier_career or career == "-":
#                         if food == applier_food or food == "-":
#                             if applier_score >= score:
#                                 meet += 1

#         answer.append(meet)

#     return answer


solution(["java backend junior pizza 150","python frontend senior chicken 210","python frontend senior chicken 150","cpp backend senior pizza 260","java backend junior chicken 80","python backend senior chicken 50"], ["java and backend and junior and pizza 100","python and frontend and senior and chicken 200","cpp and - and senior and pizza 250","- and backend and senior and - 150","- and - and - and chicken 100","- and - and - and - 150"])
# [1,1,1,1,2,4]