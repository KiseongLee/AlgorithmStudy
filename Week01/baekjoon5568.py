import itertools
n = int(input())
k = int(input())

c=[]
for i in range(n):
    c.append(int(input()))

# p = itertools.combinations(c, k)
# p = list(p)

# p = list(map(str, p))




# d=[]
# for i in range(len(p)):
#     for j in range(len(p[i])):
        
# print(d)

# def factorial(n):

#     if n <= 1 :
#         return 1
    
#     return n * factorial(n-1)

# a = factorial(n) / factorial(k)
# print(a)

res = set()
for i in list(itertools.permutations(c, k)):

    res.add(''.join(list(map(str,i))))

print(len(res))
