from collections import deque

def solution(command, arr, size):
    arr = deque(eval(arr))
    direction = True

    for c in command:
        if c == 'R':
            direction = not direction
        elif c == 'D':
            if len(arr) == 0:
                return "error"
            if direction:
                arr.popleft()
            else:
                arr.pop()

    if not direction:
        arr.reverse()

    return list(arr)

N = int(input())
for _ in range(N):
    command = input().strip()
    size = int(input())
    arr = input().strip()
    result = solution(command, arr, size)
    if result == "error":
        print("error")
    else:
        print(str(result).replace(' ', ''))

# https://www.acmicpc.net/problem/5430
