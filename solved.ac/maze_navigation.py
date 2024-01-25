from collections import deque

n, m = map(int, input().split())
maps = [list(map(int, input())) for _ in range(n)]

def solution(n,m,maps):
    q = deque()
    arrows = [[0,1],[0,-1],[-1,0],[1,0]]
    visited = [[0 for _ in range(m)] for _ in range(n)]
    visited[0][0] = 1
    q.append((0,0))

    while q:
        x,y = q.popleft()
        if x == n-1 and y == m-1:
            return visited[x][y]
        for arrow in arrows:
            nx = arrow[0] + x
            ny = arrow[1] + y
            if 0<=nx<n and 0<=ny<m:
                if visited[nx][ny] == 0 and maps[nx][ny] == 1:
                    visited[nx][ny] = visited[x][y]+1
                    q.append((nx,ny))


print(solution(n,m,maps))

# https://www.acmicpc.net/problem/2178