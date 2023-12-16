import math

def leave_sausage(sausage,user):
    leaved_sausage = sausage
    if sausage >= user:
        x = sausage // user
        leaved_sausage = sausage - (x*user)
    return leaved_sausage

def solution(sausage, user):
    leaved_sausage = leave_sausage(sausage,user)
    gcd = math.gcd(leaved_sausage, user)
    answer = user - gcd
    return answer
sausage, user = map(int, input().split())    
print(solution(sausage,user))

# or

import math
n, m = map(int,input().split())
print(m - math.gcd(n,m))


https://www.acmicpc.net/problem/1188