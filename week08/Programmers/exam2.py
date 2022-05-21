from collections import deque

def convert(n, k):
    """n을 k진수로 변환"""
    converted_num = deque()
    while n > 0:
        converted_num.appendleft(n%k)
        n //= k

    return converted_num

def make_prime_list(num):
    """소수 리스트를 만들어줌"""
    is_prime = [1]*(num+1) # 소수 리스트 만들기
    is_prime[0], is_prime[1] = 0, 0
    for i in range(num+1):
        if is_prime[i]: # 소수이면
            for j in range(2*i, num+1, i):
                is_prime[j] = 0
    return is_prime

def solution(n, k):

    converted_num = convert(n, k)

    splited = ''.join(map(str, converted_num)).split('0')

    nums = []
    for num in splited:
        if num: # 비어있지 않은 경우만
            nums.append(int(num))
    
    max_num = max(nums)
    
    if max_num >= 2:
        is_prime = make_prime_list(max_num)
    else:
        return 0

    ans = 0
    for num in nums:
        if is_prime[num]:
            ans += 1
    
    return ans