
n = int(input())

a=[]
for i in range(n):
    a.append(input())

a = set(a)
a = list(a)
# print(a)

b = []
for i in range(len(a)):
    b.append((a[i],len(a[i])))


# print(b)

def setting(data):
    return data[0], data[1]

result = sorted(b, key = lambda x : (x[1], x[0]))

# print(result)


for i in range(len(result)):
    print(result[i][0])