def solution(priorities, location):
    answer = 0
    answer = 0
    num = 0
    while priorities.count(0) != len(priorities):
        max_priority = max(priorities)
        if priorities[num] == max_priority:
            answer += 1
            priorities[num] = 0
            if num == location:
                break
            
        num += 1
        if num == len(priorities):
            num = 0
   
    return answer