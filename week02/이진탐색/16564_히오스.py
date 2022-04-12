
'''
문제 : 최대 팀 목표레벨 T를 구하자

입력 : N [1, 100만] , K [1, 10억] // 각 캐릭터의 레벨 X1, X2, ...

출력 : 최대 팀 목표레벨 출력 T = min(Xi)  i = [1, N]


'''


# n, k = map(int, input().split())

# x=[]
# for i in range(n):
#     x.append(int(input()))

# x.sort()

# x_minus = []
# for i in range(n-1):
    
#     x_minus.append(x[i+1]-x[i])


# print(x[0:3])
    
# for i in range(1,n):
    
#     while x[i+1] != x[i]:
#         x[0:i]
#         k -= 1*(i+1)
#         print(x)
#         print(k)





n, k = map(int, input().split())

data = []
for i in range(n):
    data.append(int(input()))


data.sort()


def check(level):
    result = 0
    for i in range(n):
        if data[i] < level:
            result += level - data[i]
    return result
        
def binary_sort(target, start, end):

    while start <= end:
        
        mid = (start+end)//2
        
        get = check(mid)
        
        if get == target:
            return mid
    
        elif get < target:
            start = mid + 1
        
        else:
            end = mid -1
            
    return end


print(binary_sort(k, data[0], data[n-1]))

