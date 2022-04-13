n = int(input())

map =[[0 for i in range(n)] for i in range(n)]

def recursive(n):
   
   global map 
    
   if n == 3:
       map[0][:3] = map[2][:3] = [1]*3
       map[1][:3] = [1, 0, 1]
       return

    
   size = n // 3
   recursive(n//3)
   for i in range(3):
       for j in range(3):
           if i == 1 and j == 1:
               continue
           for k in range(size):
                map[size*i+k][size*j:size*(j+1)] = map[k][:size]

    


recursive(n)

for i in range(len(map)):
    for j in range(len(map[0])):
        if map[i][j] == 1:
            print('*', end= '')
        else:
            print(' ', end = '')
    print()