prices = [1, 2, 3, 2, 3]

def solution(prices):


    answer = []
    for i in range(len(prices)):
        count = 0
        for j in range(i+1, len(prices)):
            # print(answer)
            if prices[i] > prices[j]:
                count +=1
                answer.append(count)
                break
            count += 1
        else:
            answer.append(count)

    return answer

# stack 사용

def solution(prices):
    stack = []
    answer =[0]*len(prices)
    for i in range(len(prices)):
        while stack != [] and stack[-1][1] > prices[i]: # stack의 마지막 값을 들어올 값과 비교해서 크면 answer에 시간 계산을 해준다.
                                                        # 새로 들어오는 값이기 때문에 전에 것도 다 돌려주기 위해서 while문을 사용.
                                                        # stack이 하나씩 빠지면서 계산 가능하다.
            idx, value = stack.pop()
            answer[idx] = i - idx
        stack.append([i, prices[i]])
    for i, v in stack:
        answer[i] = len(prices) - 1 - i # 끝까지 나보다 작은애들이 안나온 것이므로 끝의 인덱스에서 내것 인덱스를 빼주면 시간이 나오겠지?
    return answer