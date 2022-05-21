
# def X(n, q):
#     rev_base = ''

#     while n > 0:
#         n, mod = divmod(n, q)
#         rev_base += str(mod)
    
    
#     return rev_base[::-1]
#     # 역순인 진수를 뒤집어 줘야 원래 변환 하고자하는 base가 출력



# def is_prime_num(n):
#     for i in range(2, n):
#         if n% i ==0:
#             return False
#     return True

# ans2=[]
# ans = list(X(n,q))
# for i in range(len(ans)):
#     if ans[i] == 0:
#        ans2.append(ans[:i])
#        ans2.append(ans[i])
#     ans2.append[i+1:]

# ans3 =[]
# for i in range(len(ans2)):
#     ans3.append(int(ans2[i]))

# count = 0
# for i in range(len(ans3)):
#     if is_prime_num(ans3[i]):
#         if ans3[i-1] == 0 and ans3[i+1] == 0:
#             count +=1
#     if is_prime_num(ans3[i]): 
        
import math
def X(n, k):    # 진법 바꾸기
    rev_base = ''
    while n > 0:
        n, mod = divmod(n, k)
        rev_base += str(mod)
    return rev_base[::-1] # 외워놓기

def is_prime_num(n):    # 소수 판별
    if n == 0 or n == 1:
        return False
    for i in range(2, int(math.sqrt(n))+1):
        if n% i ==0:
            return False
    return True

def solution(n, k):
    count = 0
    ans = X(n,k).split("0")
    print(ans)
    for i in range(len(ans)):
        if ans[i] == '':
            continue
        if is_prime_num(int(ans[i])) == True:
            count += 1
    return count

n = int(input())
k = int(input())
print(solution(n,k))

# return 값을 잘 처리해주기
# 함수 하나하나씩 찍어보기
# 함수를 분리해서 쓸 수도 있다.
