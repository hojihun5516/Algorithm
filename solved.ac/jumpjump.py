import sys
input = sys.stdin.readline

def solution(N, datas):
    dp = [1000 for _ in range(N)]
    dp[0] = 0
    
    for i in range(N):
        for j in range(1, datas[i]+1):
            if i+j >= N:
                break    
            dp[i+j] = min(dp[i+j], dp[i]+1)
    return dp[N-1] if dp[N-1] != 1000 else -1
    
N = int(input())
datas = list(map(int, input().split()))
print(solution(N,datas))

# https://www.acmicpc.net/problem/11060