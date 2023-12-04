import sys

input = sys.stdin.readline
N = int(input())
numbers = list(map(int, input().split()))
numbers.sort()
max_count = int(input())

dp = [float("inf") for i in range(numbers[-1]*max_count+2)]

for i in range(1,numbers[-1]*max_count+2):
    if i in numbers:
        dp[i] = 1
    else:
        for j in range(0,i+1):        
            dp[i] = min(dp[i], dp[j]+dp[i-j])
    if dp[i]>max_count:
        s = "holsoon" if i%2==0 else "jjaksoon"
        print(f"{s} win at {i}")
        break
        


https://www.acmicpc.net/problem/1679

