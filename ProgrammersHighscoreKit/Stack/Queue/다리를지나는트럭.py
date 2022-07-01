bridge_length = 2	
weight = 10	
truck_weights = [7,4,5,6]	
def solution(bridge_length, weight, truck_weights):
    
    time = 1
    running = []
    complete = []
    wait = []
    flag = False
    
    for i in range(len(truck_weights)):
        wait.append([truck_weights[i], 0])
    print(wait)
    while True:
        
        if wait:
            if flag == False:
                x = wait.pop(0)
        
        sum = 0
        if running:
            for i in running:
                sum += i[0]
         
        if weight - (x[0]+ sum) >= 0:
            running.append(x)
            
        if running:
            for i in running:
                i[1] += 1  
                    
        for i in running:
            if  i[1] == bridge_length:
                if running:
                    y = running.pop(0)
                    complete.append(y)
        time += 1
            
        if len(complete) == bridge_length:
            break
            
    print(running)
    print(complete)
            
    return time


solution(bridge_length, weight, truck_weights)