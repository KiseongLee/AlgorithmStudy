'''
문제 : 사대의 위치와 동물들의 위치가 주어졌을 때, 동물의 수를 출력하는 프로그램 작성

입력 :사대의 수 M[1, 100,000] 동물의 수 N[1, 100,000], 사정거리[1, 10억] // 사대의 위치 M개의 x좌표 // N개 각 동물의 사는 위치(x,y) [1,10억]

출력 : 잡을 수 있는 동물의 수

조건 : 사정거리 L 이라고 하면, 사대에서 사정거리가 L보다 작거나 같은 위치의 동물들을 잡을 수 있음
      (x,0) (a, b) --> L => |x-a| + b 안에 들어오면 잡을 수 있는 동물이다.

'''
import sys
input = sys.stdin.readline
m, n, l = map(int, input().split())

x = list(map(int, input().split()))

x.sort()

count = 0

def binary_sort(array, target, start, end):
    
    while start <= end:
        
        mid = (start+end)//2
        
        if array[mid] == target:
            return array[mid]
        
        elif array[mid] < target:
            start = mid +1
        
        else:
            end = mid -1
    
    if end != 0 or (m-1):
        if abs(target - array[end])  > abs(target - array[end+1]):
            return array[end+1]
        else:
            return array[end]
    else: 
        return array[end]
        

            
def check(x):
    global count
    if l >=  abs(x-a) + b:
        count += 1        
    
    
for i in range(n):
    a, b = map(int, input().split())
    
    result = binary_sort(x, a, 0, m-1)
    
    check(result)

print(count)


