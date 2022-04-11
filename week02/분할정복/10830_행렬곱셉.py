'''
문제 : 크기가 N*N인 행렬 A가 주어진다. A의 B제곱을 구하는 프로그램을 작성

입력 : 행렬 크기 N [2, 5], 제곱 값인 B[1, 천억] // N개의 줄에 행렬의 각 원소

출력 : 첫째 줄부터 N개의 줄에 걸쳐 행렬 A를 B제곱한 결과를 1000으로 나눈 나머지를 출력한다.

1. 행렬의 제곱에 대한 식을 써보고 분할할 수 있으면 분할해서 식을 써야할 것

2. 분할 --> 재귀함수 구현 // 재귀 종료 조건 알아야함.

3. 식쓰기

'''
n, b = map(int, input().split())

data = [list(map(int, input().split())) for _ in range(n)]

b = bin(b)[2:] # 2진법으로 전환


def mul(a, b):
    
    result = [[0]*n for i in range(n)]
    
    for i in range(n):
        for j in range(n):
            for k in range(n):
                result[i][j] += a[i][k] * b[k][j]
                
    for i in range(n):
        for  j in range(n):
            result[i][j] %= 1000
    
    return result


identify_matrix = [[1 if i==j else 0 for i in range(n)] for j in range(n)]

result = identify_matrix[:]
for i in range(len(b)):
    if b[-i-1] == '1':
        temp = data[:]
        while i != 0:
            temp = mul(temp, temp)
            i -= 1
        result = mul(result, temp)

for row in result:
    print(*row)