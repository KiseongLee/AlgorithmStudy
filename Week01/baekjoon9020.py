# import math
# x = 10000

# def prime(x):

#     if x == 1 or x == 0:
#         return False

#     for i in range(2, int(math.sqrt(x))+1):
#         if x % i == 0:
#             return False
#     return True

# a = []
# for i in range(x):
#     if prime(i):
        
#        a.append(i)


# n = int(input())
# for i in range(n):
#     c = int(input())
#     b = 0
#     while a[b] < c:
#       b += 1
#     print(a[b-1], c - a[b-1])

import math
t = int(input())

def prime(x):
    if x == 1 or x == 0:
        return False

    for i in range(2, int(math.sqrt(x)+1)):
        if x % i == 0:
            return False
    return True

for i in range(t):
    n = int(input())

    a = n/2
    b = n/2

    while True:

        if prime(a) and prime(b) :
            print(int(a), int(b))
            break

        else:
            a -= 1
            b += 1