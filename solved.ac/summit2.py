import sys
N = int(input())
dp = [0] * (N+1)

div = 987654321

dp[0] = 1
dp[2] = 1

for i in range(4, N+1, 2):
    plus = 0
    for j in range(0, i//2, 2):
        left = j
        right = i - j - 2
        if left != right:
            plus += dp[left] * dp[right] *2
        else:
            plus += dp[left] * dp[right]
    dp[i] = plus% div
print(dp[N])

# https://www.acmicpc.net/problem/1670