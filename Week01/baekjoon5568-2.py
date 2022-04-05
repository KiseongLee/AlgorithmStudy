import itertools

n = int(input())
k = int(input())

data = []
for i in range(n):
    data.append(input())

permutation = list(itertools.permutations(data, k))
x = []

result = set(permutation)
result = list(result)

# ------------------------------------------------------
'''
result2 = []
for i in result:
  result2.append(''.join(list(i)))

result = set(result2)
result2 = list(result)

print(len(result2))
'''
# --------------------------------------------------------


a = ""
for i in range(len(result)):
    for j in range(k):
        a += result[i][j]
    x.append(a)
    a = ""

result_final = set(x)
x = list(result_final)
print(len(x))
