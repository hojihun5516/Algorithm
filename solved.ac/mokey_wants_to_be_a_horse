import heapq

def add_padding(array):
    rows = len(array)
    cols = len(array[0])
    
    new_array = [[1] * (cols + 4) for _ in range(rows + 4)]

    for i in range(rows):
        for j in range(cols):
            new_array[i + 2][j + 2] = array[i][j]

    return new_array

def solution(arr, r, c, k):
    horse_moving = [[-2,-1],[-1,-2],[1,-2],[2,-1],[2,1],[1,2],[-1,2],[-2,1]]
    monkey_moving = [[0,1],[1,0],[-1,0],[0,-1]]

    visited = [[[False for _ in range(c + 4)] for _ in range(r + 4)] for _ in range(k + 1)]
    que = []
    
    heapq.heappush(que, (0, 2, 2, 0))  # (count, row, col, chance)
    visited[0][2][2] = True
    answer = -1
    
    while que:
        count, row, col, chance = heapq.heappop(que)

        if row == r + 1 and col == c + 1:
            answer = count
            break

        for moving in monkey_moving:
            cur_row = row + moving[0]
            cur_col = col + moving[1]
            if arr[cur_row][cur_col] != 1 and not visited[chance][cur_row][cur_col]:
                visited[chance][cur_row][cur_col] = True
                heapq.heappush(que, (count + 1, cur_row, cur_col, chance))
                
        if chance < k:
            for moving in horse_moving:
                cur_row = row + moving[0]
                cur_col = col + moving[1]
                if arr[cur_row][cur_col] != 1 and not visited[chance + 1][cur_row][cur_col]:
                    visited[chance + 1][cur_row][cur_col] = True
                    heapq.heappush(que, (count + 1, cur_row, cur_col, chance + 1))

    return answer if answer != -1 else -1

# 입력 받는 부분
K = int(input())
col, row = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(row)]
padded_arr = add_padding(arr)
result = solution(padded_arr, row, col, K)
print(result)

# https://www.acmicpc.net/problem/1600