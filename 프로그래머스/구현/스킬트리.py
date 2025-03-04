def solution(skill, skill_trees):
    answer = 0
    
    for skill_tree in skill_trees:
        skill_temp = skill
        
        for s in skill_tree:
            idx = skill_temp.find(s)
            if idx == 0:
                if len(skill_temp) > 0:
                    skill_temp = skill_temp[1:]
            elif idx > 0:
                break
        else:
            answer += 1
            
    return answer