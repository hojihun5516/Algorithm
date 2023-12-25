import sys
input = sys.stdin.readline

def solution(row, col, arr):
    dp = [[0 for _ in range(col)] for _ in range(row)]
    
    for i in range(row):
        for j in range(col):
            if i-1 >= 0 and j-1 >= 0:
                dp[i][j] = max(dp[i-1][j], dp[i][j-1]) + arr[i][j]
            elif i-1>=0 and j-1<0:
                dp[i][j] = dp[i-1][j] + arr[i][j]
            elif i-1<0 and j-1>=0:
                dp[i][j] = dp[i][j-1] + arr[i][j]
            else:
                dp[i][j] = arr[i][j]
    return dp[row-1][col-1]
    
row, col = map(int, input().split())
arr = []
for _ in range(row):
    arr.append(list(map(int,input().split())))

print(solution(row,col,arr))


# https://www.acmicpc.net/problem/14430