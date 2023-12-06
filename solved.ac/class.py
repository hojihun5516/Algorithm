import sys
import heapq
input = sys.stdin.readline

N = int(input())
classes = [list(map(int, input().split())) for _ in range(N)]
classes.sort(key = lambda x:x[1])

cnt = 0
mh = []
for cl in classes:
    while mh and mh[0]<=cl[1]:
        heapq.heappop(mh)
    heapq.heappush(mh, cl[2])
    cnt = max(cnt, len(mh))
print(cnt)

https://www.acmicpc.net/problem/1374