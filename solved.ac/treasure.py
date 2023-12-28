import sys
input = sys.stdin.readline

def solution(A,B,N):
    A.sort()
    B.sort(reverse=True)
    answer = 0
    for i in range(N):
        answer+= (A[i] * B[i])
    return answer

N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

print(solution(A,B,N))

# https://www.acmicpc.net/problem/1026