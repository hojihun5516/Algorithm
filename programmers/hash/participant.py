import collections

def solution(participant, completion):
    answer = collections.Counter(participant) - collections.Counter(completion)
    return list(answer.keys())[0]

# https://school.programmers.co.kr/learn/courses/30/lessons/42576
