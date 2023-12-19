import sys
input = sys.stdin.readline

def solution(oven, pizzas):
    new_oven = create_new_oven(oven)
    i = len(new_oven) - 1
    pizza_i = 0
    pizza_check = 0
    
    while i>=0:
        if pizzas[pizza_i]<=new_oven[i]:
            pizza_i+=1
            pizza_check+=1
        if pizza_i == len(pizzas):
            break
        i-=1
        
    if pizza_i != len(pizzas):
        return 0
    return i+1

def create_new_oven(oven):
    new_oven = []
    new_oven.append(oven[0])
    for i in range(1, len(oven)):
        if oven[i] > new_oven[i-1]:
            new_oven.append(new_oven[i-1])
        else:
            new_oven.append(oven[i])
    return new_oven

D, N = map(int, input().split())
oven = list(map(int, input().split()))
pizzas = list(map(int, input().split()))

print(solution(oven, pizzas))


# https://www.acmicpc.net/problem/1756