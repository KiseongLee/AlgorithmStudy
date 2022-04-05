import sys
input = sys.stdin.readline

n = int(input().rstrip())
k = int(input().rstrip())

cards_array = [input().rstrip() for _ in range(n)]
array = set()

def permutation(cnt, perm, visit):
    
    global cards_array
    
    if cnt == k :                       # k만큼 뽑고 문자열을 합치겠다는 의미
        array.add(''.join(perm))
        return
    
    for idx in range(n):                
        if not visit[idx]:
            visit[idx] = 1
            permutation(cnt+1, perm+[cards_array[idx]], visit)
            visit[idx] = 0
            

permutation(0, [], [0]*n)

print(array)



























'''
1. 몇개 중에 몇개 뽑을 것인가 입력 받아야함

2. 그리고 배열을 받아야함

3. 이제 하나씩 뽑는 재귀 함수를 구현해야함

   - 첫번째 : 몇개 뽑았을 때, 그 값들을 합쳐서 뽑아낸다. (join)
            그런데 중복되는 것은 뺀다 (set)
   - 두번째 : 방문 처리를 이용하여 재귀함수를 구현한다.
            일단 처음 뽑는 것을 방문 처리 해준다.
            그리고 카운트를 하나 늘려서 재귀를 돌린다 / per이라는 배열에서 합쳐줘야한다.
            방문 처리 한 것을 False로 만들어주고 함수를 종료한다.
'''
'''
n = int(input())
k = int(input())

card_arr = []
for i in range(n):
    card_arr.append(input())

arr = set()

def recursion(cnt, per, visit):
    
    if cnt == k:
        arr.add("".join(per))             #add라는 것을 써야함 (집합 자료형이기 때문이다.) append or insert는 리스트에 사용
        return
    
    for i in range(n):
        if not visit[i]:
            visit[i] = True
            recursion(cnt+1, per+card_arr[i], visit)
            visit[i] = False


recursion(0, [], [False]*n)
'''