import math
n = int(input())
a = list(map(int, (input().split())))


def prime(x):

    if x == 1:
        return False

    for i in range(2, int(math.sqrt(x))+1):
       if x % i == 0:
           return False
    return True


count = 0
for i in range(n):
    if prime(a[i]):
        count += 1

    
print(count)