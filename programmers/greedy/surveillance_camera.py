def solution(routes):
    answer = 0
    routes.sort(key=lambda x: x[1])
    camera = -30001
    for route in routes:
        if camera < route[0]:
            answer += 1
            camera = route[1]
    return answer

# https://school.programmers.co.kr/learn/courses/30/lessons/42884