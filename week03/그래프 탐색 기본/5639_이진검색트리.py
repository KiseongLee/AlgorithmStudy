'''
1. 입력으로 전위 순회한 결과가 주어진다.

2. 입력값의 개수가 주어져 있지 않다.

3. 노드의 수가 정확하게 주어져 있지 않다(10000 이하) 따라서, 입력 받는 방법도 중요

4. 루트/왼/오로 되어 있는 것을 왼/오/루트로 출력

 - preorder = [] 전위 순회한 결과를 담기위한 그릇
 - while, try ~ except 문을 통해 입력값이 들어올 때 까지 입력받음.

function : postorder(start, end)
 - 배열의 인덱스를 돌며 후위 순회 진행
 - root = preorder[start]
   -> 루트 노드로 설정
 - 배열을 돌며 오른자식 노드의 위치(idx)를 찾는다
 - start = start + 1, end = idx // start = idx, end = end
 - 새롭게 두 part로 나눠서 재귀함수 호출
 - print(root) >> 후위 순회이므로 보내고 나서 루트노드 출력
 - if start >= end : return 배열을 모두 돌면 return
 

'''

import sys

sys.setrecursionlimit(10 ** 9)

preorder = []


def postorder(nums):
    length = len(nums)
    
    if length <= 1:
        return nums

    for i in range(1, length):
        if nums[i] > nums[0]:
            return postorder(nums[1:i]) + postorder(nums[i:]) + [nums[0]]
    
    return postorder(nums[1:]) + [nums[0]]


while True:
    try:
        preorder.append(int(sys.stdin.readline()))
    except:
        break

preorder = postorder(preorder)

for n in preorder:
    print(n)
    
    
# https://rccode.tistory.com/entry/Python-%EB%B0%B1%EC%A4%80-5639%EB%B2%88-%EC%9D%B4%EC%A7%84-%EA%B2%80%EC%83%89-%ED%8A%B8%EB%A6%AC


