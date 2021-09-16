def solution(skill, skill_trees):
    answer = 0
    
    for skill_tree in skill_trees:
        skillidx = [30 for _ in range(len(skill))]
        noskill = 0
        for idx, value in enumerate(skill_tree):
            for num, val in enumerate(skill):

                if val == value:
                    skillidx[num] = idx
                    break
            else:
                noskill += 1
        for sk in range(len(skillidx)-1):
            if skillidx[sk] > skillidx[sk+1]:
                break
        else:
            answer += 1
            
    return answer