import sys
sys.setrecursionlimit(10 ** 9)

n = int(input())
inorder = list(map(int, input().split()))
postorder = list(map(int, input().split()))
position = [0]*(n+1)


for i in range(n):
    position[inorder[i]] = i                # 후위 순회의 끝값이 중위 순회의 어디 인덱스에 위치한지 확인하기 위해
                                            # 중위 순회의 값들의 인덱스값을 저장한다.

# 분할 정복 방식으로 전위 순회를 찾음
def preorder(in_start, in_end, post_start, post_end):
    # 재귀 종료 조건(수렴)   
    if (in_start > in_end) or (post_start > post_end):
        return
    
    # 후위 순회 결과의 끝이 (서브)트리의 루트임을 이용
    parents = postorder[post_end]
    print(parents, end = " ")
    
    # 중위 순회에서 루트의 좌 우로 자식들이 갈라지는 것을 이용하여 left, right 선언
    # inorder에서 정점의 인덱스를 알고 있으면 left자식의 개수, right쪽 자식의 개수를 알 수 있다.
    left = position[parents] - in_start
    right = in_end - position[parents]
    
    # left, right로 나눠 분할 정복 방식으로 트리를 추적하여 전위 순회를 찾아냄
    preorder(in_start, in_start+left-1, post_start, post_start+left-1) # 왼쪽 서브트리
    preorder(in_end-right+1, in_end, post_end-right, post_end-1) # 오른쪽 서브트리

# 중위 순회, 후위 순회 모두 0부터 n-1 (전체 범위)값을 주고 전위 순회를 구함
preorder(0, n-1, 0, n-1)    


# 1. 핵심은 중위 순회, 후위 순회가 다 필요하다는 것이다

# 2. 일단 중위 순회에서 루트 값이 어디에 나오는지를 알아야하기 때문에 position이라는 리스트를 만들고
# 후위 순회의 끝 값이 중위 순회의 어디 인덱스에 위치하는지 확인할 수 있다.

# 3. 재귀 함수에서 값을 총 4개를 받는다. 중위 순회 리스트의 인덱스 시작값부터 끝값까지, 후위 순회 리스트의 인덱스 시작값부터 끝값까지

# 4. 재귀 종료 조건은 이진탐색 하듯이 start가 end 보다 커지면 끝나도록 한다

# 5. 후위 순회의 끝값이 parents라고 정의하고 바로 출력한다 (전위 순회는 루트 먼저 출력하므로)

# 6. 후위 순회의 끝값이 어디 위치에 있는지 알기위해 position값을 받아왔기 때문에 여기의 position[parents]값이
#    중위 순회의 루트 인덱스 값이 되므로 왼쪽 오른쪽 자식의 개수를 알 수 있다
#    left = position[parents] - in_start
#    right = in_end - position[parents]

# 7. 왼쪽 부분에서 똑같이 재귀를 돌려주면 루트노드먼저 출력되면서 나뉘겠지?
#    오른쪽 부분에서 똑같이 재귀를 돌려주면 루트노드먼저 출력되면서 나뉘겠지? 반복

# 8. 여기서 핵심은 후위 순회, 중위 순회 모두 인덱스 값이 필요하다는 것인데
#    후위 순회는 1) 루트값 print 2) 중위 순회의 루트 인덱스 값이 어디인지 알기 위함이고
#    중위 순회는 1) left, right값을 나눠서 left 자식, right 자식의 개수를 알기 위함이다.





# https://velog.io/@bae_mung/Python-BOJ-2263-%ED%8A%B8%EB%A6%AC%EC%9D%98-%EC%88%9C%ED%9A%8C
# https://sujeng97.tistory.com/6
