from collections import deque

n = int(input())
def solution(n):
    if n < 10:
        return n-1

    result = []
    que = deque()
    for i in range(1,11):
        que.append(i)
        result.append(i-1)

    while que:
        cur = que.popleft()
        for i in range(0,cur%10):
            que.append(int(str(cur)+str(i)))
            result.append(int(str(cur)+str(i)))
        if len(result) > n-1:
            return result[n-1]
    return -1

print(solution(n))

# https://www.acmicpc.net/problem/1174
# bfs로 접근하였고, 맨뒤의 수보다 작은 수만 붙여주는 for i in range(0,cur%10): 이 부분이 핵심이다