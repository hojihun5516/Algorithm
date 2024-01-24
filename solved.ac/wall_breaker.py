from collections import deque

n,m = map(int, input().split())
graph = []
for i in range(n):
    graph.append(list(map(int, input())))

def solution(n,m,graph):
    visited = [[[0] * 2 for _ in range(m)] for _ in range(n)]    
    visited[0][0][0] = 1
    q = deque()
    q.append((0,0,0))
    arrows = [[0,1],[0,-1],[1,0],[-1,0]]
    
    while q:
        x,y,used = q.popleft()
        if x == n-1 and y == m-1:
            return visited[x][y][used]
        for arrow in arrows:
            nx = x + arrow[0]
            ny = y + arrow[1]
            if 0<=nx<n and 0<=ny<m:
                # 한번도 부수지 않았고 다음 블럭이 벽이다
                if used==0 and graph[nx][ny] == 1:
                    visited[nx][ny][1] = visited[x][y][0] + 1
                    q.append((nx,ny,1))
                elif graph[nx][ny] == 0 and visited[nx][ny][used] == 0:
                    visited[nx][ny][used] = visited[x][y][used] + 1
                    q.append((nx,ny,used))
    return -1
    

print(solution(n,m,graph))

# https://www.acmicpc.net/problem/2206