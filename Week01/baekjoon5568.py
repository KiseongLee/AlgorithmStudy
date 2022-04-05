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

    res.add(''.join(list(map(str,i))))          # join 리스트를 문자열로 일정하게 합쳐준다.
                                                # '구분자' .join(리스트) --> ''.join이면 리스트를 ['a', 'b', 'c'] 이런 식의 리스트를 'abc'의 문자열로 합쳐서 반환


print(len(res))
