import sys
def solution(n):
    graph = [int(sys.stdin.readline()) for _ in range(n)]
    answers = []
    if n==1:
        return [1]
    else:
        #맨 앞의 경우
        if graph[0]>=graph[1]:
            answers.append(1)
            
        #for문으로 가운데 
        for i in range(1,n-1):
            if graph[i - 1] <= graph[i] and graph[i] >= graph[i + 1]:
                answers.append(i+1)
        #마지막
        if graph[n-2]<=graph[n-1]:
            answers.append(n)
    return answers
n = int(sys.stdin.readline())
result = solution(n)
for data in result:
    print(data)
# print(solution(n))

https://www.acmicpc.net/problem/2232