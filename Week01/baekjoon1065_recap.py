import sys
input = sys.stdin.readline

n = int(input())



count = 0
for i in range(1, n+1):
    
    if  i <= 99:
       count += 1
       
    
    else: 
        
      a = str(i)
    
      if int(a[1])-int(a[0]) == int(a[2])-int(a[1]):
              count += 1
    
print(count)