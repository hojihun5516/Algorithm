def solution(special):
    stack = []
    for s in special:
        if not stack:
            stack.append(s)
        else:
            if s == ")" and stack[-1] == "(":
                stack.pop()
            else:
                stack.append(s)
    if stack:
        return False
    return True

# https://school.programmers.co.kr/learn/courses/30/lessons/12909