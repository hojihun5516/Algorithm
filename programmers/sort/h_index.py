def solution(citations):
    citations.sort()
    n = len(citations)
    for i,c in enumerate(citations):
        if c >= n-i:
            return n - i
    return 0

# https://school.programmers.co.kr/learn/courses/30/lessons/42747