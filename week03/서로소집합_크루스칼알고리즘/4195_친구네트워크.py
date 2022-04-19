import sys
input = sys.stdin.readline

def find(parent, x):
    
    if parent[x] != x:        # 부모 테이블에서 x라는 key의 value값이 x가 같지 않으면
        parent[x] = find(parent, parent[x]) # 부모 테이블에서 x라는 key의 value값은 = find() --> 재귀함수 진행
    return parent[x]            # 부모테이블에서 x라는 key와 value값이 같아 질 때, value값이 return 된다. 위로 올려서 대입하면
                                # x라는 이름(key)의 value 값들이 갱신된다

def union(parent, a, b):    # union 함수 a = 이름, b = 이름
    a = find(parent, a)     # a = find값 함수 --> 부모 테이블에서 a라는 key의 value인데 부모 값이겠지
    b = find(parent, b)     # b = find값 함수 --> 부모 테이블에서 b라는 key의 value인데 부모 값이겠지
    
    if a != b :             # 같지 않으면
       parent[b] = a        # key!!! // b의 value 값들을 a라는 값으로 바꾸는데 이건 a의 부모 값이겠지
       number[a] += number[b] # a의 숫자에 b의 숫자를 더해버린다.

t = int(input())        # 테스트 케이스 입력 받음

for i in range(t):
    parent = dict()     # 이름이 나오니까 dictionary로 무조건 받아야함
    number = dict()     # 숫자는 count할 것 ==> 출력을 뽑아야 하므로
                
    f = int(input())    # 친구 관계 수 입력 받음

    for i in range(f):  
        x,y= input().split()    # 친구 이름 각각 입력
        
        if x not in parent:     # x 친구 이름이 부모테이블에 없으면
            parent[x] = x       # 부모 테이블에 이름 넣고
            number[x] = 1       # 숫자를 1로 넣어준다 (처음 나온것이기 떄문)
                                # ex) parent =  {'Fred' : 'Fred', 'Barney' : 'Barney'}
                                # ex) number =  {'Fred' : 1, 'Barney' : 1}
        
        if  y not in parent:    # 위와 마찬가지로 작성
            parent[y] = y
            number[y] = 1
            
        union(parent, x,y)      # union 함수 생성
        print(number[find(parent, x)])
                                
        
        
            