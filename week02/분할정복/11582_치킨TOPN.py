import sys
input = sys.stdin.readline

def recursion(arr, n, k):
    if len(arr) == 1:
        return
    recursion(arr[:len(arr)//2], n, k)
    recursion(arr[len(arr)//2:], n, k)
    if len(arr)//2 == n//k:
        a = arr[:len(arr)//2]
        b = arr[len(arr)//2:]
        a.sort()
        b.sort()
        arr = a + b
    
        print(*arr,end=" ")

n = int(input())
arr = list(map(int, input().split()))
k = int(input())

recursion(arr, n, k)




'''
n=int(input().strip())
n_list=list(map(int,input().strip().split()))
k=int(input().strip())
new_list=[]

for i in range(0,n,n//k):
    new_list += sorted(n_list[i:i+n//k])
    
print(" ".join(str(i) for i in new_list))
'''


'''
1. len(arr) == 1 재귀 종료 조건 걸어주고
2. 병합정렬 재귀식 적어주면 된다.
나누기 2하면 되겠지.
3. 이제 뽑아낼 것을 정하면 되는데, 내가 입력한 값을 넣었을 때 그만큼 병합 정렬이 되어있어야 한ㄴ거니까
len 길이는 어떻게 하면 될까? 생각해보면 되겠지
그리고 
'''


def sort(arr, n, k):
    
    if len(arr) == 1:
        return
    
    sort(arr[:len(arr)//2], n, k)
    sort(arr[len(arr)//2:], n, k)
    
    if len(arr)//2 == n//k:         # 생각을 해보면 k가 2가 들어오면 4개씩 정렬이 되야한다
                                    # 4개씩 정렬이 되려면 len(arr)가 4가 되면
                                    # 밑에식에서 2로 나눠버리면서 2개씩 정렬이 되어버림
                                    # 따라서 a, b의 개수가 n//k이어야 하므로 
                                    # len(arr)//2 = n//k이어야 한다
                                    # 헷갈리지 말도록
        a = arr[:len(arr)//2]
        b = arr[len(arr)//2:]
        a.sort()
        b.sort()
        
        output = a + b
        
        return print(*output, end = " ")

n = int(input())

arr = list(map(int, input().split()))
k = int(input())

sort(arr, n, k)