n, c = map(int, input().split())

array=[]
for i in range(n):
    array.append(int(input()))

array.sort()

start = 1
end = array[-1] - array[0]
answer = 0


while start <= end:
    
    mid = (start+end)//2                    
    current = array[0]                      
    count = 1                               # 공유기의 개수가 주어지므로 count해서 세워야함
      
    for i in range(1, len(array)):          # 집의 개수만큼 for문을 돌린다.
        if array[i] >= current + mid:       # 공유기를 설치할 위치 >= 현재의 위치 + 이진탐색으로 찾아낸 공유기 사이의 거리
            count += 1                      # 조건을 만족하면 count를 세준다(공유기의 개수가 주어지므로) // count 1인 이유는 무조건 처음에 설치해야 거리가 최대!!
            current = array[i]              # 현재의 위치 = 조건을 만족하는 공유기 설치할 위치로 초기화 하면서 더해나간다.
            

    if count >= c:                          # count 값이 설치할 공유기의 개수를 넘어가면 --> 이진 탐색으로 더 딱맞는 거리를 찾아보자
        start = mid + 1                     # 거리를 늘리기 위해서 start = mid + 1로 준다.
        answer = mid                        # 답 뽑을 때, mid 값에 없을 수도 있는데 이게 답이 되는지가 궁금합니다.
    else:
               
        end = mid - 1                       # 설치할 공유기 개수가 만족되지 않으면, 거리를 조금 더 줄여서 다시 탐색해보자.

print(answer)

'''
문제의 핵심 key :

공유기를 설치할 위치 = 현재 위치 + 이진탐색으로 찾아낸 공유기 거리

'''



