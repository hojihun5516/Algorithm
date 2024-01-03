def solution(answers):
    answer = []
    one = "12345" * 2000
    two = "21232425" * 2000
    three = "3311224455" * 2000
    
    count = [0,0,0]
    for i,ans in enumerate(answers):
        count[0] += 1 if int(one[i]) == ans else 0
        count[1] += 1 if int(two[i]) == ans else 0
        count[2] += 1 if int(three[i]) == ans else 0
    
    max_count = max(count)
    answer = []
    for i, c in enumerate(count):
        if c == max_count:
            answer.append(i+1)
    return answer
# https://school.programmers.co.kr/learn/courses/30/lessons/42840