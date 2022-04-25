import sys
input = sys.stdin.readline

def solution(food_times, k):
    
    food_times = list(map(int, input().split()))
    k = int(input().rstrip())
    answer = 0
    
    for i in range(k+1):
 
        if i >= len(food_times):
           i = i - len(food_times)
       
        while True:
            if food_times[i] == 0:
               i += 1
               if i >= len(food_times):
                  i = i - len(food_times)
        
            else:
                break
        
        food_times[i] -= 1
        answer = i +1
    
    return answer



