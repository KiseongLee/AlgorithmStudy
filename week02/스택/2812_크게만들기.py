'''
문제 : N자리 숫자가 주어졌을 때, 여기서 K개를 지워서 얻을 수 있는 가장 큰 수를 구하는 프로그램 작성

입력 : N (k, 500,000]  k [1, 500,000] // N자리 숫자가 주어진다.(이 수는 0으로 시작하지 않는다.)

출력 : 입력으로 주어진 숫자에서 k를 지웠을 때 얻을 수 있는 가장 큰 수 출력

조건 : stack의 개념을 활용해보아라.

일단 앞에 스택 문제와 비슷하게 규칙을 찾아내는 문제인 거 같다.
괄호도 그렇고 막대기, 탑 다 결국 stack에서 넣었다 빼낼 때 or 새로운 걸 넣었을 때 규칙을 바꿔서 답을 구해낸 것인데
탑은 크기 비교 했을 떄, 어떻게 되면 빼고 아니면 넣고 이런게 있는데

여기서도 똑같은 느낌이지만 새로운 상황이라서 어려움을 느낌

크게 만들어야 하므로
숫자 비교가 필요할 것 같음

일단 stack에 넣어보자 
모든 예제를

1) 앞 숫자가 가장 큰 값이 나올 때까지 count --> 큰 값은 따로 넣어둠
예외 : 첫 숫자가 가장 크면? 
이거 stack으로 구현 가능할 거 같다.
--> 구현
2) 인덱스를 받아와야함 생각해보니

'''
import sys
input = sys.stdin.readline
n, k = map(int, input().split())

a = input().strip()

a = list(map(int, a))


stack = []
stack1 = []
stack2 = []
count = 0
overlap = 0

for i in range(n):
    
    if stack:
        
        if stack[-1][1] < a[i]:
            
            if overlap >= k:
                break
            
            else:
                stack.pop()
                stack.append([i, a[i]])
                count += 1 + overlap
                overlap = 0
        
        elif stack[-1][1] == a[i]:
             stack.pop()
             stack.append([i, a[i]])
             overlap += 1
        
        else:
            count += 1
        
        if count == k:
            break
    
    
    else:
        stack.append([i, a[i]])
    

count = stack[0][0] - overlap

for _ in range(overlap+1):
    stack1.append(stack[0][1])
    
# print(stack1)

b = stack[0][0]+1
overlap = 0
for i in range(b, n):
    
    if count >= k:
        for j in range(i, n):
            stack2.append(a[j])
        break
    
    if stack2:
        
        if stack2[-1] < a[i]:
            stack2.pop()
            stack2.append(a[i])
            count += 1
            
        elif stack[-1] == a[i]:
            stack2.append(a[i])
        
        else:
            count += 1
        
        if count == k:
            for j in range(i+1, n):
                stack2.append(a[j])
            break
    
    else:
        stack2.append(a[i])

# print(stack2)

total_stack = stack1 + stack2

total_stack = list(map(str, total_stack))
# print(total_stack)
print(("".join(total_stack)))