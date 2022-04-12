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

start = 0                           # 배열의 index값이다
end = n-1

answer = data[start] + data[end]    # 처음 비교를 위해서 answer라는 변수를 만들고 값을 더함 // start는 data의 첫값, end는 data의 마지막값

left = start                        #정답 받아오는 용도의 변수 처리
right = end                         
    
while start < end:    # = 붙이면 틀림....왜그러지???  -> ex) data를 1,2,3,4,5를 받았다고 해보자
                      #                                 그렇게 되면 이진 탐색을 했을 때, 계속해서 end -= 1을 받을 것이다(다 양수고 오름차순이므로)
                      #                                 그러다가 start와 end값이 같게 될 때, 사이클이 돌아버리면 data[start] = data[end]가
                      #                                 되므로 오류가 되어버린다. 정리 잘해놓기
        
    value = data[start] + data[end]  # 비교를 위한 value값 생성

    if abs(value) < abs(answer):     # 앞에서 받았던 answer와 value를 비교한다
        
        answer = value               # value값이 작으면 answer값을 교체한다. 
        left = start                 # left값은 start
        right = end                  # right값은 end
        
        if answer == 0:              # answer == 0 이면 바로 출력
            break
        
    if value < 0:                    # value값이 작으면
        start += 1                   # start값이 1씩 증가하면서 -값을 줄이도록 해본다
    
    else:
        end -= 1                    # end값이 1씩 줄어들면서 +값을 줄이도록 해본다
    

print(data[left], data[right])      # 오름 차순이므로 left, right 순으로 출력

#https://bdbest.tistory.com/92

