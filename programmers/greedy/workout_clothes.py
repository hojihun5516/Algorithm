def solution(n, lost, reserve):
    students = [1 for i in range(n)]
    for l in lost:
        students[l-1] = 0
    for r in reserve:
        students[r-1] += 1
    
    i=0
    while i!=n:
        if students[i] == 0:
            if i>0 and students[i-1] == 2:
                students[i-1] = 1
                students[i] = 1
            elif i < n-1 and students[i+1] == 2:
                students[i] = 1
                students[i+1] = 1
        i+=1
    return n - students.count(0)

# https://school.programmers.co.kr/learn/courses/30/lessons/42862