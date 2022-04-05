def move(n, start, to):
    print(n, start, to)
    
def hanoi(n, start, to, via):
    
    if n == 1:
        move(1, start, to)
    
    else:
        hanoi(n-1, start, via, to)
        move(n, start, to)
        hanoi(n-1, via, to, start)

n = int(input())

hanoi(3, 1, 3, 2)