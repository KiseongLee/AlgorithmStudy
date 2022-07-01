# 1차 시도
'''
채점 결과
정확성: 96.4
합계: 96.4 / 100.0
'''

from itertools import combinations

def solution(clothes):
    
    hash_map ={}
    for cloth in clothes:
        if cloth[1] in hash_map:  
            hash_map[cloth[1]] += 1
        else:
            hash_map[cloth[1]] = 1  
    
    sum = 0
    ans = 1
    hash_map_list = list(hash_map.values())
    for i in range(len(hash_map_list)):
        hash_map_list_cob = list(combinations(hash_map_list, i+1))
        for h in hash_map_list_cob:
            for i in h:
                ans *= i
            sum += ans
            ans = 1
            
    return sum

# 2차 시도
'''
채점 결과
정확성: 96.4
합계: 96.4 / 100.0
'''
from itertools import combinations
def multiply(arr):
    return eval('*'.join([str(n) for n in arr]))


def solution(clothes):
    
    hash_map ={}
    for cloth in clothes:
        if cloth[1] in hash_map:  
            hash_map[cloth[1]] += 1
        else:
            hash_map[cloth[1]] = 1
    
    sum = 0
    ans = 1
    hash_map_list = list(hash_map.values())
    for i in range(len(hash_map_list)):
        hash_map_list_cob = list(combinations(hash_map_list, i+1))
        for h in hash_map_list_cob:
            
            sum += multiply(h)

    return sum

#3차시도
'''
채점 결과
정확성: 96.4
합계: 96.4 / 100.0
'''
from itertools import combinations
from functools import reduce

def multiply(arr):
    return reduce(lambda x, y: x * y, arr)


def solution(clothes):
    
    hash_map ={}
    for cloth in clothes:
        if cloth[1] in hash_map:  
            hash_map[cloth[1]] += 1
        else:
            hash_map[cloth[1]] = 1
    
    sum = 0
    ans = 1
    hash_map_list = list(hash_map.values())
    for i in range(len(hash_map_list)):
        hash_map_list_cob = list(combinations(hash_map_list, i+1))
        for h in hash_map_list_cob:
            
            sum += multiply(h)

    return sum


# 답안



def solution(clothes):
    
    hash_map ={}
    for cloth in clothes:
        if cloth[1] in hash_map:  
            hash_map[cloth[1]] += 1
        else:
            hash_map[cloth[1]] = 1
    
    ans = 1     # 하나도 안입는 경우를 1로 빼주면 되는 문제 괜히 조합까지 가져옴
    for h in hash_map:
        ans *= hash_map[h]+1

    return ans-1