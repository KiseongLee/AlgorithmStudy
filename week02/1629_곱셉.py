'''
문제 : 자연수 A를 B번 곱한 수에 C로 나눈 나머지를 구하자 

입력 : 첫째 줄에 A,B,C가 빈 칸을 사이에 두고 주어진다 [1, 2,147,483,647]

출력 : 첫째 줄에 A를 B번 곱한 수를 C로 나눈 나머지 출력

무조건 분할을 해서 풀어야함. 왜나하면 a, b, c값이 21억이 되기 떄문에

a^b = a^(b/2) + a^(b/2)로 나눠서 풀면 되겠다.
    = (a^(b/2))^2로 하면 보일 것
    = 재귀 종료 조건은 b=1 이 되겠다.

'''

def divide(a, b, c):
    
    if b == 1:
        return a % c
    
    
    if b % 2 == 0 :
        return (divide(a, b//2, c) ** 2) % c
    
    else:
        return (divide(a, b//2, c)**2 *a ) % c


a, b, c = map(int, input().split())

print(divide(a, b, c))