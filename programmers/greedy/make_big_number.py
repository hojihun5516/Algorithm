def solution(number, k):
    stack = []
    
    for n in list(number):
        if not stack:
            stack.append(n)
        else:
            while stack and stack[-1] < n and k>0:
                k-=1
                stack.pop()
            stack.append(n)
    
    if k > 0:
        stack = stack[:-k]
    return "".join(stack)

# https://school.programmers.co.kr/learn/courses/30/lessons/42883