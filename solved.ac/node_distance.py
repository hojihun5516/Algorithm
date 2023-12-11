from collections import deque

def solution(nodes, start, end):
    que = deque()
    que.append([start, 0, set()])
    answer = []
    while que:
        current_node, cost, visited = que.popleft()
        for target_node, target_cost in nodes[current_node]:
            if target_node not in visited:
                cur_visited = visited.copy()
                cur_visited.add(target_node)
                current_cost = target_cost + cost
                if target_node == end:
                    answer.append(current_cost)
                else:
                    que.append([target_node, current_cost, cur_visited])
    return min(answer)

N,M = map(int, input().split())
nodes = {i:[] for i in range(1,N+1)}
for _ in range(N-1):
    start, end, distance = map(int, input().split())
    nodes[start].append([end, distance])
    nodes[end].append([start, distance])

for _ in range(M):
    start,end = map(int, input().split())
    print(solution(nodes,start,end))


# https://www.acmicpc.net/problem/1240
# answer에 값을 전부 넣고 최소값만 리턴하여 구했다