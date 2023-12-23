import heapq

def solution(s,e):
    q = []
    positions = set()
    heapq.heappush(q,(0,s))
    answer = 0
    while q:
        count, position = heapq.heappop(q)
        if position == e:
            answer = count
            break
            
        if position+1 <= e and position+1 not in positions:
            heapq.heappush(q,(count+1, position+1))
            positions.add(position+1)
        
        if 0 <= position-1 and position-1 not in positions:
            heapq.heappush(q,(count+1, position-1))
            positions.add(position-1)
            
        if position*2 <= e*2 and position*2 not in positions:
            heapq.heappush(q,(count+1, position*2))
            positions.add(position*2)
    return answer

s, e = map(int,input().split())
print(solution(s,e))


# https://www.acmicpc.net/problem/1697