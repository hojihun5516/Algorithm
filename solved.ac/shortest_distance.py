import sys
import heapq

input = sys.stdin.readline

V, E = map(int, input().split())
K = int(input())
INF = int(1e9)

def make_graph(E):
    graph = {i+1:[] for i in range(V)}
    for _ in range(E):
        s, e, c = map(int, input().split())
        graph[s].append([e,c])
    return graph

def solution(start, graph, V):
    q = []
    heapq.heappush(q, (0, start))
    distance = [INF] * (V+1)
    distance[start] = 0

    while q:
        dist, current = heapq.heappop(q)

        if distance[current] < dist:
            continue
            
        for i in graph[current]:
            cost = dist + i[1]

            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))
    
    return distance

graph = make_graph(E)
distance = solution(K, graph, V)

for i in range(1, V+1):
    if distance[i] == INF:
        print("INF")
    else:
        print(distance[i])

# https://www.acmicpc.net/problem/1753