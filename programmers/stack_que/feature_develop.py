def solution(progresses, speeds):
    answer = []
    due_dates = []
    for p, s in zip(progresses,speeds):
        least = 100 - p
        if least % s == 0:
            due_dates.append(least // s)
        else:
            due_dates.append((least // s) +1)
    
    stack = []
    stack.append(due_dates[0])
    for d in due_dates[1:]:
        if stack[0] >= d:
            stack.append(d)
        else:
            answer.append(len(stack))
            stack = []
            stack.append(d)
    answer.append(len(stack))
    return answer

    # https://school.programmers.co.kr/learn/courses/30/lessons/42586