import sys
input = sys.stdin.readline

def solution(N, A):
    dp = [1 for _ in range(N)]
    for i in range(N):
        for j in range(i):
            if A[j] < A[i]:
                dp[i] = max(dp[i], dp[j]+1)
    return max(dp)

N = int(input())
A = list(map(int, input().split()))

print(solution(N,A))


# https://www.acmicpc.net/problem/11053
