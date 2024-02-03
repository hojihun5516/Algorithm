n,m = map(int, input().split())
maps = [list(map(int, input().split())) for _ in range(n)]

def solution(maps):
    new_map = [[0 for _ in range(len(maps[0]))] for _ in range(len(maps))]
    new_map[0][0] = maps[0][0]

    for i in range(len(maps)):
        for j in range(len(maps[0])):
            if i>0 and j > 0 :
                new_map[i][j] = max(new_map[i-1][j],new_map[i][j-1]) +  maps[i][j]
            elif i> 0 and j == 0:
                new_map[i][j] = new_map[i-1][j] +  maps[i][j]
            else:
                new_map[i][j] = new_map[i][j-1] +  maps[i][j]
    return new_map[len(maps)-1][len(maps[0])-1]

print(solution(maps))
    
# https://www.acmicpc.net/problem/11048