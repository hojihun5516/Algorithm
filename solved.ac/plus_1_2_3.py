def solution(max_num):
    dp = [0 for _ in range(max_num)]

    dp[0] = 1
    dp[1] = 1
    dp[2] = 2
    dp[3] = 4

    for i in range(4,max_num):
        dp[i] = sum(dp[i-3:i])
    return dp
    
n = int(input())
arr = [int(input()) for _ in range(n)]

result = solution(max(arr)+1)
for i in arr:
    print(result[i])
    
# https://www.acmicpc.net/problem/9095