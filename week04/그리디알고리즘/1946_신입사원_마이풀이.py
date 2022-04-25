import sys
input = sys.stdin.readline

t = int(input())


for i in range(t):
   n = int(input())
   new=[]
   for i in range(n):
       a, b = map(int, input().split())
       new.append((a,b))
   new.sort()
       
   X = new[0][1]
   count = 1
   for i in range(n):
        if X > new[i][1]:
            count += 1
            X = new[i][1]
   print(count)

