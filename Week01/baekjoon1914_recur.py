
'''
하노이의 탑에서 재귀를 발견해야하는데

hanoi(n)에서 hanoi(n-1)을 2개 발견할 수 있다.
첫번쨰로는 hanoi(n-1)에서 두개의 원판은 B원반에 이미 꽂혀 있어야한다.
두번째로는 hanoi(n-1)에서 3번째 원판을 C원반에 꽂혀있어야 한다.
재귀 후(나머지 원반을 다 B로 옮기고), 가장 큰 원반을 목적지로 옮기고, 다시 마지막 재귀를 통해 n-1개의 원반을 목적지에 옮긴다.

첫번째 : n-1개의 원반을 'a'에서 'b'로 옮긴다.
두번째 : n-1개의 원반을 'b'에서 'c'로 옮긴다.

두 재귀는 옮기는 원반의 개수는 같지만 원반을 움직이는 출발지와 목적지가 다르다.
우리의 문제 정의에서 출력은 각 움직임의 출발지와 목적지도 같이 기술해야하기 때문에 함수에서 이 두 정보를 같이 추적해줘야한다.

원반 개수, 출발지, 목적지 --> 변수로 받아야함

여기에 경유점이라는 개념도 추가된다. 
'A'에서 'C'로 3개의 원반을 이동할 때 'B' 막대도 결국 사용해야한다. 이렇게 세 개의 입력을 같이 입력해줘야 원반을 하나씩 이동할 때 경유점을 지날 때도 문제없이 출력할 수 있다.

예외, N=1일 때 자신의 위에 원반이 없기 때문에 재귀가 필요없고 바로 원반을 옮기고 종료한다.
이 것이 곧 재귀함수의 탈출 조건이다. 

hanoi(n, start, to, via):

    if n == 1:
        move(1, start, to)
    else:
        hanoi(n-1, start, via, to)  첫번째 재귀에서는 맨 밑의 n번째 원반을 목적지로 옮기기 위해 위의 n-1개의 원반을 경유지로 옮긴다
        move(n, start, to)          그 다음 n 번째 원반을 목적지로 옮긴다.
        hanoi(n-1, via, to, start)  경유지에 있는 n-1개 원반을 to로 옮긴다.
'''



def move(n, start, to):
    print(n, start, to)
    
def hanoi(n, start, to, via):
    
    if n == 1:
        move(1, start, to)
    
    else:
        hanoi(n-1, start, via, to)
        move(n, start, to)
        hanoi(n-1, via, to, start)

n = int(input())

hanoi(3, 1, 3, 2)



    
# def hanoi(n, start, to, via):
    
    
        
#     if n == 1:
#         print(start, to)
    
#     else:
#         hanoi(n-1, start, via, to)
#         print(start, to)
#         hanoi(n-1, via, to, start)

# n = int(input())

# if n > 20:
    
#     print(2**n-1)
# else:
#     print(2**n-1)
#     hanoi(n, 1, 3, 2)    
    
    
    
    
    



def hanoi(n, start, to, via):
    global count
    if n == 1:
        print(1, start, to)
        count += 1
    
    else:
        hanoi(n-1, start, via, to)
        print(n, start, to)
        count += 1
        hanoi(n-1, via, to, start)

n= int(input())
count = 0
hanoi(n, "A", "C", "B")
print(count)

# https://shoark7.github.io/programming/algorithm/tower-of-hanoi