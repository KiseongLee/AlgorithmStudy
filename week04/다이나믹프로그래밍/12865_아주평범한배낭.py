n, k = map(int, input().split())

data = []
D = [0] * (k+1)
for i in range(n):
    weight, value = map(int, input().split())
    data.append([weight, value])

data.sort()

for i in range(k, data[0][0]-1, -1):
    D[i] = data[0][1]
    

for i in range(1, len(data)):
    for j in range(k, data[i][0]-1, -1):
        D[j] = max(D[j], D[j-data[i][0]]+data[i][1])

print(D[-1])


# 거꾸로 와야 배낭 중복처리가 안된다. 
# 앞에서부터 하면 배낭 중복처리가 되면서 난리가 난다.
# 생각만 바꾸면 되는 문제였다...
# D[6] = D[3] + value