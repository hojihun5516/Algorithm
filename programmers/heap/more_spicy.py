import heapq

def solution(scoville, K):
    q = []
    answer = 0
    for s in scoville:
        heapq.heappush(q,(s))

    while q:
        point1 = heapq.heappop(q)
        if point1>=K:
            break
        
        if len(q)>0:
            point2 = heapq.heappop(q)
            temp = point1 + (2*point2) 
            heapq.heappush(q,(temp))
            answer+=1
        else:
            return -1
    return answer


# https://school.programmers.co.kr/learn/courses/30/lessons/42626