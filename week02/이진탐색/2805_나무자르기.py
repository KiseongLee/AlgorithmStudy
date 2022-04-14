'''
2805번 나무 자르기 문제


문제 : 적어도 M미터의 나무를 집에 가져가기 위해 절단기에 설정할 수 있는 높이의 최댓값을 구하는 프로그램

입력 : 나무의 수 N  [1, 1,000,000]// 필요한 나무 길이 M [1, 2,000,000,000]
	나무의 높이 (나무의 수만큼) [0, 1,000,000,000]

출력 : 적어도 M미터의 나무를 집에 가져가기 위해서 절단기에 설정할 수 있는 높이의 최댓값 출력.

조건 : 절단기 설정 높이 이하이면, 잘리지 않는다. 


일단 나열을 해, 그리고 이진 탐색으로 잘라보자 자른 값들의 합을 구해야하므로 생각을 해야겠다.


1. 이진 탐색을 시작한다.
array는 받고, target은 계산을 해야하겠지. start값과, end값은 정해져있고,

array에 있는 값들에서 array[mid]값들을 빼서 그 나머지들의 합을 구하면 될 거 같다.

가장 중요한 것은 합이 딱 될 때, 구하면 좋은데 넘을 때랑 구분하는 지점이 정하기 어려울거같음.

start가 end 조건을 넘을 때라는 것은 모든 탐색을 마치고 더 이상 진행할 수 없다는 뜻이므로
이 때, array[mid]값을 가져오면 되겠다.
'''
# 내가 푼 풀이 
# import copy
# n, m = map(int, input().split())

# data = list(map(int, input().split()))

# data.sort()

# def binary_sort(array, target, start, end):
    
#     mid = (start+end) // 2
    
#     if start > end:
#         return mid
    
#     array2 = copy.deepcopy(array)
    
  
    
#     for i in range(n):
#         array2[i] -= mid
#         if array2[i]<0:
#             array2[i] = 0 
#     sum_array = sum(array2)
    
        
#     if sum_array == target:
#         return mid
    
#     elif sum_array < target:
#         return binary_sort(array, target, start, mid-1)
    
#     else:
#         return binary_sort(array, target, mid+1, end)
    

# print(binary_sort(data, m, 0, data[n-1]))



#정답 풀이

# 1. 체크 함수
# 2. 이진 탐색
# 재귀 함수는 메모리를 많이 먹을 수 밖에 없는 구조여서 반복문으로 고쳐 보려고 한다. 밑에 작성
'''
n, m = map(int, input().split())

data = list(map(int, input().split()))

data.sort()


def check(height):
    result = 0
    for i in range(n):
        if data[i] > height:
            result += data[i] - height
    return result
        
def binary_sort(array, target, start, end):
    
    mid = (start+end)//2
    
    if start > end:
        return mid
    
    get = check(mid)
    
    if get == target:
        return mid
    
    elif get < target:
        return binary_sort(array, target, start, mid-1)
    
    else:
        return binary_sort(array, target, mid+1, end)

print(binary_sort(data, m, 0, data[n-1]))
'''

# n, m = map(int, input().split())

# data = list(map(int, input().split()))

# data.sort()


# def check(height):
#     result = 0
#     for i in range(n):
#         if data[i] > height:
#             result += data[i] - height
#     return result
        
# def binary_sort(target, start, end):

#     while start <= end:
        
#         mid = (start+end)//2
        
#         get = check(mid)
        
#         if get == target:
#             return mid
    
#         elif get < target:
#             end = mid -1
        
#         else:
#             start = mid + 1
            
#     return end


# print(binary_sort(m, 0, data[n-1]))



n, m = map(int, input().split())

data = list(map(int, input().split()))

data.sort()

def check(height):
    result = 0
    for i in range(n):
        if data[i] > height:
            result += data[i] - height
    return result

def binary_sort(target, start, end):

    while start <= end:
        
        mid = (start+end)//2
               
        
        if check(mid) >= target:
            start = mid + 1
        
        else:
            
            end = mid -1
            
    return end

print(binary_sort(m, 0, data[n-1]))