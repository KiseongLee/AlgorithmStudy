bridge_length = 2	
weight = 10	
truck_weights = [7,4,5,6]	


# answer = 0
# bridge = [0 for _ in range(bridge_length)]

# while bridge:
    
#     answer += 1
#     bridge.pop(0)
    
#     if truck_weights:
#         if sum(bridge) + truck_weights[0] <= weight:
#             t = truck_weights.pop(0)
#             bridge.append(t)
#         else:
#             bridge.append(0)
            
# print(answer)


def solution(bridge_length, weight, truck_weights):
    
    answer = 0
    bridge = [0 for i in range(bridge_length)]
    
    while bridge:
        answer += 1
        bridge.pop(0)
        
        if truck_weights:
            print(truck_weights)
            if sum(bridge) + truck_weights[0] <= weight:
               t = truck_weights.pop(0)
               bridge.append(t)
            else:
               bridge.append(0)

        
    print(bridge)
    
    return print(answer)

solution(bridge_length, weight, truck_weights)