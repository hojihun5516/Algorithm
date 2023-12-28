import sys
import heapq

def dijkstra(start, N, nodes):
    distances = [sys.maxsize for _ in range(N+1)]
    distances[start] = 0
    queue = [(0, start)]

    while queue:
        current_distance, current_node = heapq.heappop(queue)

        if distances[current_node] < current_distance:
            continue

        for neighbor, weight in nodes[current_node]:
            distance = current_distance + weight
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(queue, (distance, neighbor))
    return distances

def solution(N, M, X, arr):
    nodes_to_X = {i:[] for i in range(1, N+1)}
    nodes_from_X = {i:[] for i in range(1, N+1)}

    for start, end, time in arr:
        nodes_to_X[start].append((end, time))
        nodes_from_X[end].append((start, time))
    
    distances_from_X = dijkstra(X, N, nodes_to_X)

    distances_to_X = dijkstra(X, N, nodes_from_X)

    max_time = max(distances_to_X[i] + distances_from_X[i] for i in range(1, N+1))

    return max_time
print(solution(N, M, X, arr))

# https://www.acmicpc.net/problem/1238