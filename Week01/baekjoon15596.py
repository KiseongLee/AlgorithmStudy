n = int(input())
a = []
for i in range(n):
    a.append(i)

sum = 0
def sum_int(a: list) -> int:

    for i in a:
        sum += i
    
    print(sum)


def solve(a):
    sum = 0
    for i in a:
        sum += i
    
    return sum