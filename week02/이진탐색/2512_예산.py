# n = int(input())

# data = list(map(int, input().split()))

# m = int(input())

# data.sort()


# start = 0           ##핵심!! 큰 값에서 더욱 안가는 거에서 막히다가 품. 큰 값에서 조건이 if에 안걸리고 else에 걸리다가 끝나버리니까 문제가 됬는데
#                     ## start값을 아예 0으로 잡아버리면 문제가 해결됨
# end = data[-1]
# ans = 0

# def check(money):

#     result = 0
#     for i in range(n):
#         if money <= data[i]:
#             result += money
#         else:
#             result += data[i]
#     return result



# while start <= end:
    
#     mid = (start+end)//2
    
#     if check(mid) <= m:
#         start = mid + 1
#         ans = mid
    
#     else:
#         end = mid - 1
        
        

# print(ans)


n = int(input())

data = list(map(int, input().split()))

m = int(input())

data.sort()

start = 0
end = data[-1]


ans = 0

def check(money):
    result = 0
    for i in range(n):
        if data[i] >= money:
            result += money 
        else:
            result += data[i]
    
    return result


while start <= end:
    
    mid = (start+end)//2
    
    if check(mid) <= m:
        ans = mid
        start = mid +1
        
    else:
        end = mid - 1

print(ans)