def solution(num): 
    num = list(map(str, num))
    num.sort(key = lambda x : x*3, reverse = True) 
    return str(int(''.join(num)))

# https://school.programmers.co.kr/learn/courses/30/lessons/42746