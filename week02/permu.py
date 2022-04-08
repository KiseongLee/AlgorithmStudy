'''
array = list(map(int, input().split()))

n = int(input())

visited = []
count = 0
def per(value, visited):
    global count
    if len(visited) == n :
        print(visited)
        count += 1
        
    
    for i in range(len(array)):
        if not array[i] in visited:
            visited.append(array[i])
            per(value+array[i], visited)
            visited.pop()
    

per(0, visited)
print(count)
'''

'''
조합 = visited 빼도됨
array = list(map(int, input().split()))

n = int(input())
visited =[]
count = 0
def com(value, idx):
    global count
    
    if len(visited) == n:
        count += 1
    
   
    for i in range(len(array)):
         if idx < i:
            visited.append(array[i])
            print(visited)
            com(value+array[i], i)
            visited.pop()


com(0, -1)
print(count)
'''
