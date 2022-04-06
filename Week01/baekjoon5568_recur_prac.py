import sys
n = int(input())
k = int(input())

card_arr = []
for i in range(n):
    card_arr.append(sys.stdin.readline().rstrip())            #rstrip()을 안해주면 뒤에 \n가 들어간다. 주의
                                                              # input 보다는 sys.stdin.readline()이 빠르다.
                                                              

arr = set()

def recursion(cnt, per, visit):         
    
    if cnt == k:
        arr.add("".join(per))             #add라는 것을 써야함 (집합 자료형이기 때문이다.) append or insert는 리스트에 사용
        return
    
    for i in range(n):
        if not visit[i]:                                   #
            visit[i] = True
            recursion(cnt+1, per+[card_arr[i]], visit)     #리스트 끼리 더할 때는 서로 리스트 여야 한다
            visit[i] = False


recursion(0, [], [False]*n)
print(arr) 