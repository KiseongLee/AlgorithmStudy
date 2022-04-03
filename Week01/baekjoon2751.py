# import sys
# sys.setrecursionlimit(10**6)
# n = int(input())

# data = []
# for i in range(n):
#     data.append(int(input()))

# def quick_sort(data, start, end):

#     if start >= end :
#         return

#     pivot = start
#     left = start + 1
#     right = end

#     while left <= right:

#         while left <= end and data[left] <= data[pivot]:
#             left += 1

#         while right > start and data[right] >= data[pivot]:
#             right -=1
        
#         if left > right:
#             data[pivot], data[right] = data[right], data[pivot]
        
#         else:
#             data[left], data[right] = data[right], data[left]
    
#     quick_sort(data, start, right-1)
#     quick_sort(data, right+1, end)

# quick_sort(data, 0, len(data)-1)

# for i in data:
#     sys.stdout.write(str(i)+'\n')

# 퀵정렬은 최악의 경우 시간 복잡도가 O(N2)이기 때문에 퀵정렬로 문제를 풀지 말라

# import sys

# n = int(sys.stdin.readline().rstrip())

# arr = []
# for i in range(n):
#     arr.append(int(input()))


# def merge_sort(arr):
#     if len(arr) <= 1:
#         return arr

#     mid = len(arr)//2


#     left = merge_sort(arr[:mid])
#     right = merge_sort(arr[mid:])
#     return merge(left, right)

# def merge(left, right):
#     i = 0
#     j = 0
#     arr =[]

#     while (i<len(left)) and (j<len(right)):
#         if left[i] < right[j]:
#             arr.append(left[i])
#             i += 1
#         else:
#             arr.append(right[j])
#             j += 1
    
#     while (i<len(left)):
#         arr.append(left[i])
#         i += 1
    
#     while (j<len(right)):
#         arr.append(right[i])
#         j += 1
    
#     return arr

# arr = merge_sort(arr)

# for i in arr:
#     sys.stdout.write(str(i)+'\n')


# 병합 정렬

def merge_sort(array): 

    if len(array)<=1: 
        return array 
    mid = len(array)//2 
    left = merge_sort(array[:mid]) 
    right = merge_sort(array[mid:]) 
    
    i, j, k = 0, 0, 0
    
    while i < len(left) and j < len(right): 
        if left[i] < right[j]: 
            array[k] = left[i]
            i+=1 
        else:
            array[k] = right[j]
            j += 1
        k += 1
        
    if i == len(left):
        while j < len(right):
            array[k] = right[j]
            j += 1
            k += 1
    elif j == len(right):
        while i < len(left):
            array[k] = left[i]
            i += 1
            k += 1
    return array


N = int(input()) 
arr=[]

for _ in range(N): 
    arr.append(int(input())) 

arr = merge_sort(arr)

for i in arr: 
    print(i)





