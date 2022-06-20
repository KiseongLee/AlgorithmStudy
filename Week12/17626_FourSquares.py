import math

n = int(input())
n_root = int(math.sqrt(n))
d = [4]*(n+1)
d[0]=0

for i in range(1, n_root+1):
    for j in range(i**2, n+1):
                d[j] = min(d[j], d[j-(i**2)]+1)
print(d[n])


# for문을 전체적으로 한 번 돌리면서 
# 나보다 작은 제곱수들을 빼면서 갱신을 해주면 된다.

# n = int(input())
# d = [0]*(n+1)
# d[1] = 1
# for i in range(2, n+1):
#     min_value = 1e9
#     j = 1
    
#     while (j**2) <= i:
#         min_value = min(min_value, d[i-(j**2)])
#         j += 1
#     d[i] = min_value + 1

# print(d)