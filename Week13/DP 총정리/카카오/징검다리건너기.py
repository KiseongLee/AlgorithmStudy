def solution(stones, k):
    
    answer = 0
    count = 0
    check = [0] * k
    while True:
        for i in range(len(stones)):
            stones[i] -= 1
            if stones[i] <= 0:
                stones[i] = 0
            
            if stones[i] == 0:
                count += 1
                continue
        answer += 1
        for i in range(len(stones)-k):
           
           if stones[i:i+k] == check:
                print(stones)
                return answer

        # print(answer, stones)
        

# https://wiselog.tistory.com/65



def solution(stones, k):
    
    answer = 0
    count = 0
    check = [0] * k
    while True:
        for i in range(len(stones)):
            stones[i] -= 1
            if stones[i] <= 0:
                stones[i] = 0
            
            if stones[i] == 0:
                count += 1
                continue
        answer += 1
        for i in range(len(stones)-k):
           
           if stones[i:i+k] == check:
                print(stones)
                return answer

        # print(answer, stones)
        

    