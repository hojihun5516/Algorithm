import heapq

def solution(operations):
    q = []
    for o in operations:
        if "I" in o:
            num = int(o.split(" ")[1])
            heapq.heappush(q, (num))
        elif "D 1" == o and q:
            q = q[:-1]
        elif "D -1" == o and q:
            q = q[1:]
    if q:
        return [max(q), min(q)]
    return [0,0]

# https://school.programmers.co.kr/learn/courses/30/lessons/42628