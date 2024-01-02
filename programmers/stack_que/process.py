from collections import deque

def solution(priorities, location):
    sorted_priorities = deque(sorted(priorities, reverse=True))
    new_priorities = deque()
    for i,p in enumerate(priorities):
        new_priorities.append((i,p))
    answer = 0
    while sorted_priorities:
        i, cur = new_priorities.popleft()
        
        if sorted_priorities[0] == cur:
            answer+=1
            sorted_priorities.popleft()
            if i == location:
                return answer
        else:
            new_priorities.append((i,cur))

# https://school.programmers.co.kr/learn/courses/30/lessons/42587