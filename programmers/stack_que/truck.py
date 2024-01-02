def solution(bridge_length, weight, truck_weights):
    
    answer = 0
    bridge = [0 for _ in range(bridge_length)]
    summed = 0
    while bridge:
        
        answer += 1
        a = bridge.pop(0)
        summed-=a
        
        if truck_weights:
            if summed + truck_weights[0] <= weight:            
                t = truck_weights.pop(0)
                bridge.append(t)
                summed+=t
            else:
                bridge.append(0)
                 
    return answer

    # https://school.programmers.co.kr/learn/courses/30/lessons/42583