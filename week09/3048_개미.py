# 개미 구현 문제
# 1) 배열을 받은 뒤, 합친다 (Right 쪽은 거꾸로 받아야함)
# 2) 오른쪽 가는 것은 1, 왼쪽으로 가는 것은 0을 가지고 다니게한다
# 3) 그리고 ans, ans2 두 개의 배열을 만든다
# 4) ans는 탐색용, ans2는 실제 배열이 바뀌는 용도이다
# 5) 한 번 for문 돌 때마다, ans를 ans2로 갱신해야하는데 -> 여기서 그냥 값을 넣어주면 값이 같이 가버린다
# 6) 그래서 deepcopy를 써야한다.


import copy
n1, n2 = map(int, input().split())
R = list(map(str, input()))
R.reverse()
L = list(map(str, input()))
t = int(input())

Right = []
for i in range(len(R)):
    Right.append([R[i], 1])

Left = []
for i in range(len(L)):
    Left.append([L[i], 0])

ans = Right+Left
ans2 = Right+Left

for _ in range(t):
    for i in range(len(ans)-1):
        if ans[i][1] == 1 and ans[i+1][1] == 0:
            temp = ans2[i]
            ans2[i] = ans2[i+1]
            ans2[i+1] = temp
    ans = copy.deepcopy(ans2)

for i in range(len(ans2)):
    print(ans2[i][0], end='')