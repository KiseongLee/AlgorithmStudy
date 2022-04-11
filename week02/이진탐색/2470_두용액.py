# 용액 문제

'''
문제 : 특성값이 0에 가장 가까운 용액 찾기

입력 : 전체 용액 수 N[2, 100,000] // N개의 정수 [-10억 이상 10억 이하] // 

출력 : 특성 값이 0에 가장 가까운 용액을 만들어내는 두 용액의 특성값 출력 (오름차순) 
      두 개 이상일 경우 아무것이나 하나 출력
      
조건 : 두 종류의 알칼리성이나 산성 상관없다.



'''

n = int(input())

data = list(map(int, input().split()))

data.sort()

start = 0
end = n-1

answer = data[start] + data[end]

left = start
right = end    
    
while start < end:    # = 붙이면 틀림....왜그러지???
        
    value = data[start] + data[end]
    
    if abs(value) < abs(answer):
        
        answer = value
        left = start
        right = end
        
        if answer == 0:
            break
        
    if value < 0:
        start += 1
    
    else:
        end -= 1
    

print(data[left], data[right])

#https://bdbest.tistory.com/92
    