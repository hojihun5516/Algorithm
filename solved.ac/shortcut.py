def solution(target, shortcuts):
    dp = [_ for _ in range(target+1)]    
    shortcuts.sort(key = lambda x:x[0])
    for i in range(target+1):
        dp[i] = min(dp[i], dp[i-1]+1)
        for start, end, cost in shortcuts:
            if i == start and dp[i] + cost < dp[end]:
                dp[end] = dp[i] + cost
    return dp[target]

n, target = map(int, input().split())
shortcuts = []
for _ in range(n):
    start, end, cost = map(int, input().split())
    if end-start < cost or end > target:
        continue
    shortcuts.append((start,end,cost))

print(solution(target, shortcuts))

# https://www.acmicpc.net/problem/1446