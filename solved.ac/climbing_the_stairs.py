import sys
input = sys.stdin.readline

def solution(N, stairs):
    dp = [[0 for _ in range(3)] for _ in range(N+1)]

    for i in range(1,N+1):
        dp[i][0] = max(dp[i-1][1], dp[i-1][2])
        dp[i][1] = dp[i-1][0] + stairs[i-1]
        dp[i][2] = dp[i-1][1] + stairs[i-1]
    return max(dp[i][1], dp[i][2])
        
    
N = int(input())
stairs = [int(input()) for _ in range(N)]
print(solution(N,stairs))


# https://www.acmicpc.net/problem/2579