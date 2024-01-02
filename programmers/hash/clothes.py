def solution(clothes):
    setting = {}
    answer=1
    for item, parts in clothes:
        setting[parts] = setting.get(parts, []) + [item]
    
    for v in setting.values():
        answer *= (len(v)+1)
    return answer - 1
# 가짜 item을 parts별로 하나씩 추가한다 (아무것도 안입을 경우)
# 1 을빼는 이유는 가짜 - 가짜 조합이 생길경우
    # https://school.programmers.co.kr/learn/courses/30/lessons/42578