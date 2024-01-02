from collections import Counter

def solution(nums):
    half = len(nums)//2
    counter = Counter(nums)
    poncketmon_specifics = len(counter.keys())
    for i in range(half,0,-1):
        if i <= poncketmon_specifics:
            return i
    
# https://school.programmers.co.kr/learn/courses/30/lessons/1845