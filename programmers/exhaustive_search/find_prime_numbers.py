from itertools import permutations
import math

def is_prime_number(x):
    for i in range(2, int(math.sqrt(x)) + 1):
        if x % i == 0:
            return False
    return True

def solution(numbers):
    answer = 0
    new_numbers = list(numbers)
    total = []
    for i in range(len(new_numbers)):
        all_numbers = list(permutations(new_numbers, i+1))
        all_numbers = (list(map(lambda x: int("".join(x)), all_numbers)))
        total.extend(all_numbers)
    
    total = list(set(total))
    for n in total:
        if is_prime_number(n) and n > 1:
            answer+=1
    return answer

# https://school.programmers.co.kr/learn/courses/30/lessons/42839