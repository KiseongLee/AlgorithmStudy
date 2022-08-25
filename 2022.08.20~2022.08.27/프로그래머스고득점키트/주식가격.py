def solution(prices):
    
    answer = [0] * len(prices)
    stack = []
    
    for i in range(len(prices)):
        while stack != [] and stack[-1][1] > prices[i]:
             idx, value = stack.pop()
             answer[idx] = i - idx 
        stack.append([i, prices[i]])
    for idx, value in stack:
        answer[idx] = len(prices) - 1 - idx
    return answer


def solution(prices):
    answer = [0] * len(prices)
    stack = []
    
    for i, cur in enumerate(prices):
        while stack and cur < prices[stack[-1]]:
            last = stack.pop()
            answer[last] = i - last
        stack.append(i)
        answer[i] = len(prices)-1-i
    return answer
'''
전형적인 스택 구조로 푸는 문제다
가격이 나와 있고 나중값이 전에값보다 작으면 날짜를 갱신하고,
그 외는 배열의 len값에서 계산해주면 된다.

1. (반복)stack이 존재하고, 현재값이 스택의 가장위에 있는 값보다 크다면
    - 스택 top을 pop 시킨다
    - 답의 배열에 현재 인덱스에서 스택에서 꺼낸 인덱스의 값을 뺀다
2. 이외에 stack에 인덱스 값을 넣어준다
3. answer값도 갱신해준다.
리턴으로 answer을 하면 답이나온다.
'''
