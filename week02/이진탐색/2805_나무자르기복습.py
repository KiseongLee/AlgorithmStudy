n, m = map(int, input().split())

data = list(map(int, input().split()))

data.sort()


sum = 0

def check(height):
    global sum
    sum = 0
    for i in range(n):
        if data[i] >= height:
            sum = sum + data[i] - height
        
    return sum                              # 실수 포인트 : 리턴은 for문이 끝난다음에 들어와야함

def binary_search(target, start, end):
    
    while start <= end:
        

        mid = (start+end)//2
        
        
        if check(mid) == target:
            return mid

        
        elif check(mid) > target:
            start = mid + 1                 # check값은 잘라지고 내가 얻는 값이잖아
                                            # 얻는 값이 더크면 더 잘라내야 하니까 mid값을 올려야지 그래서 start값을 올리는 것.
        else:
            end = mid -1
    
    return end                              # end값이 조건이여서 end값이 바뀌는 순간을 체크 할 수 있는 것은 end값밖에 없다.
                                            # start값이 바뀌면서 end가 출력되는 건 어떻게 되는 건가?





print(binary_search(m, 0, data[n-1]))

