import sys
from collections import deque

def dfs(row, col):
    if visited[row][col] != -1:
        return visited[row][col]

    visited[row][col] = 0

    for arrow in arrows:
        nx = arrow[0] + row
        ny = arrow[1] + col
        if 0 <= nx < map_row and 0 <= ny < map_col and maps[nx][ny] > maps[row][col]:
            visited[row][col] += dfs(nx, ny)

    return visited[row][col]

map_row, map_col = map(int, input().split())
maps = []
for _ in range(map_row):
    maps.append(list(map(int, input().split())))

visited = [[-1 for _ in range(map_col)] for _ in range(map_row)]
arrows = [[0,1],[1,0],[0,-1],[-1,0]]
visited[0][0] = 1

print(dfs(map_row - 1, map_col - 1))


# https://www.acmicpc.net/problem/1520