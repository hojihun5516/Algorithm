import sys

input = sys.stdin.readline
n = int(input())
houses = []

for i in range(n):
    line = list(map(int,input().split()))
    houses.append(line)

for i in range(1,n):
    houses[i][0]+= min(houses[i-1][1],houses[i-1][2])
    houses[i][1]+= min(houses[i-1][0],houses[i-1][2])
    houses[i][2]+= min(houses[i-1][0],houses[i-1][1])
print(min(houses[n-1]))

https://www.acmicpc.net/submit/1149/69868539
다익스트라 알고리즘