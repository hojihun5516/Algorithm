import sys
import heapq

input = sys.stdin.readline

def solution(items, bags):
    items.sort(key = lambda x:x[0])
    bags.sort()
    q = []
    item_index = 0
    total_value = 0
    for bag in bags:
        while item_index<len(items) and items[item_index][0] <= bag:
            heapq.heappush(q, -items[item_index][1])
            item_index += 1
        if q:
            total_value -= heapq.heappop(q)
    return total_value

N, K = map(int, input().split())
items = [list(map(int, input().split())) for _ in range(N)]
bags = [int(input()) for _ in range(K)]

print(solution(items, bags))

# https://www.acmicpc.net/problem/1202