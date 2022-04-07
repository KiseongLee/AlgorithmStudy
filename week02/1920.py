# 1920 번

# 문제 : N개의 정수가 주어져 있을 때, 이 안에 X라는 정수가 존재하는지 알아내는 프로그램
# 입력 : N [1, 100,000] / N개의 정수 주어짐 A[1] ''' / M [1, 100,000] / M개의 수들이 주어짐 
# 출력 : M개의 줄에 답을 출력한다. 존재하면 1 존재하지 않으면 0을 출력

#1. A의 수열을 정렬한다음

#2. 밑에 것을 하나하나씩 for문으로 이진 탐색하여 존재하면 1로 받고 0으로 받으면될듯


n = int(input())
n_data = list(map(int, input().split()))
m = int(input())
m_data = list(map(int, input().split()))

n_data.sort()


def binary_sort(array, target, start, end):
    
    if start > end:
        return 0
    
    mid = (start+end) // 2
    
    if array[mid] == target:
        return 1
    
    elif array[mid] > target:
        return binary_sort(array, target, start, mid-1)
    
    else:
        return binary_sort(array, target, mid+1, end)
        
        
total = []
for i in range(m):
    result = binary_sort(n_data, m_data[i], 0, n-1)
    total.append(result)

for i in total:
    print(i)