import sys
from collections import deque

def update_map_using_bfs(i,j,maps):
    que = deque()
    que.append((i,j))
    maps[i][j] = 0
    arrows = [[0,1],[0,-1],[1,0],[-1,0]]
    
    while que:
        r, c = que.popleft()
        for arrow in arrows:
            nx = arrow[0] + r
            ny = arrow[1] + c

            if maps[nx][ny] == 1:
                maps[nx][ny]=0
                que.append((nx,ny))

    return maps

def solution(row,col,count):
    maps = [[0 for i in range(col+1)] for j in range(row+1)]
    worms = 0
    for i in range(count):
        worm = sys.stdin.readline().split(" ")
        x, y = int(worm[0]), int(worm[1])
        maps[x][y] = 1

    for i in range(0,row):
        for j in range(0,col):
            if maps[i][j] == 1:
                maps = update_map_using_bfs(i,j,maps)
                worms+=1

    print(worms)
total_loop = int(sys.stdin.readline())
for loop in range(total_loop):
    row,col,count = sys.stdin.readline().split()
    solution(int(row),int(col),int(count))


https://www.acmicpc.net/submit/1012/69694123