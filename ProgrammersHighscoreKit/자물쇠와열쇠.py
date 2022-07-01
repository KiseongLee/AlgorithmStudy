key = [[0, 0, 0], [1, 0, 0], [0, 1, 1]]	
lock = [[1, 1, 1], [1, 1, 0], [1, 0, 1]]	

def rotate90(arr):
    return list(zip(*arr[::-1]))

def check(total, m, n):
    for i in range(n):
        for j in range(n):
            if total[m+i][m+j] != 1:
                return False
    return True
            
def attach(x,y,m,key,total):
    for i in range(m):
        for j in range(m):
            total[x+i][y+j] += key[i][j]
    # for i in range(len(total)):
    #    print(total[i])
    # print('\n')

def detach(x,y,m,key,total):
    for i in range(m):
        for j in range(m):
            total[x+i][y+j] -= key[i][j]

def solution(key, lock):
    m = len(key)
    n = len(lock)
    total = [[0]*(2*m+n) for _ in range(2*m+n)]

    for i in range(m, m+n):
        for j in range(m, m+n):
            total[i][j] = lock[i-m][j-m]
            
    rotated_key = key
    
    for _ in range(4):
        rotated_key = rotate90(rotated_key)
        for x in range(1, m+n):
            for y in range(1, m+n):
                attach(x,y,m,rotated_key,total)
                if(check(total, m, n)):
                    return True
                detach(x,y,m,rotated_key, total)
    return False

solution(key, lock)