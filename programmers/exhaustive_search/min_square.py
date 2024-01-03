def solution(sizes):
    new_sizes = [[min(size), max(size)] for size in sizes]
    a = sorted(new_sizes, key = lambda x:x[0], reverse=True)[0][0]
    b = sorted(new_sizes, key = lambda x:x[1], reverse=True)[0][1]
    return a*b

# https://school.programmers.co.kr/learn/courses/30/lessons/86491