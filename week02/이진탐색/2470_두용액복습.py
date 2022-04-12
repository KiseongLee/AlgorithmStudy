'''

핵심 key : 이진 탐색이지만 중간을 생각하지 않고 배열의 순서대로 생각
          비교를 위한 변수가 필요하다.

1. 입력 / 정렬

2. 정답 넣어줄 변수 생성

3. 비교값 생성 후, 반복 비교

4. 이진 탐색으로 반복

'''

n = int(input())

data = list(map(int, input().split()))

data.sort()

start = 0
end = n-1

answer = data[start] + data[end]

left = start
right = end

while start < end:
    
    value = data[start] + data[end]
    
    if abs(value) < abs(answer):
        answer = value
        left = start
        right = end
    
    
    if value < 0:
        start += 1
        
    else:
        end -= 1

print(data[left], data[right])