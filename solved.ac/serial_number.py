def sum_values(serial):
    summed = 0
    for i in serial:
        if i.isdigit():
            summed+=int(i)
    return summed

def solution(serials):
    sorted_serials = sorted(serials, key = lambda x:(len(x), sum_values(x), x))
    return sorted_serials

N = int(input())
serials = [input() for _ in range(N)]

sorted_serials = solution(serials)
for serial in sorted_serials:
    print(serial)


# https://www.acmicpc.net/submit/1431/70394424