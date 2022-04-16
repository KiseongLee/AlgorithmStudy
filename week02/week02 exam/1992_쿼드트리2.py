import sys
input = sys.stdin.readline
n = int(input())
a = [input().strip() for _ in range(n)]

result = ['']
def quadtree(N, x, y): # 행, 열
    start = a[x][y]
    if N == 1:
        return start
    for i in range(x, x+N):
        for j in range(y, y+N):
            if a[i][j] != start:
                lu = quadtree(N//2, x, y)
                ru = quadtree(N//2, x, y + N//2)
                ll = quadtree(N//2, x + N//2, y)
                rl = quadtree(N//2, x + N//2, y + N//2)
                total = lu+ru+ll+rl
                return f'({total})'
    return start

if n == 1:
    print(f'({a[0][0]})')
else:
    print(quadtree(n, 0, 0))