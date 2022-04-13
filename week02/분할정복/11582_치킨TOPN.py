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