import sys

input = sys.stdin.readline

def solution(n, expected):
    values = []
    expected = int(expected)
    for i in range(int(n)):
        values.append(int(input()))
    first = 1
    end = max(values)

    while first <= end:
        mid = (first + end) // 2
        count = 0
        for val in values:
            count+=(val // mid)
        if count >= expected:
            first = mid +1
        elif count < expected:
            end = mid - 1
    return end

n, expected=list(map(int, input().split(" ")))
print(solution(n, expected))

https://www.acmicpc.net/submit/1654/69749190