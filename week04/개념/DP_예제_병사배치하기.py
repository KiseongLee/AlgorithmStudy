n = int(input())

array = list(map(int, input().split()))

D = [1]*n                       # 수열에 무조건 1개는 들어갈 수 있는 것이니까,
                                # 초기값을 1로 받는다

for i in range(1, n):
    for j in range(i):
        if array[i] < array[j]:
            D[i] = max(D[i], D[j]+1)

print(len(array) - max(D))