import sys
input = sys.stdin.readline
m, n, l = map(int, input().split())

x = list(map(int, input().split()))

x.sort()

count = 0

def binary_sort(array, target, start, end):
    global count
    while start <= end:
        
        mid = (start+end)//2
        
        if l >=  abs(array[mid]-a) + b:
            count += 1  
            break
        
        if array[mid] == target:
            return array[mid]
        
        elif array[mid] < target:
            start = mid +1
        
        else:
            end = mid -1

     
    
for i in range(n):
    a, b = map(int, input().split())
    
    binary_sort(x, a, 0, m-1)
    

print(count)