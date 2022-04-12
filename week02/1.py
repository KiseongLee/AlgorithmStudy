from collections import deque

change={}
l = int(input())
for i in range(l):
    sec, direc = input().split()
    sec = int(sec)
    change[sec] = direc 

print(change.values)

for i in change.keys():
    
    print(i)
    if change[i] == "D":
        print("나이스")
        
print(change[5])
    
    
# x,y = map(int, input().split())
# for _ in range(4):
    
#     a = deque()
#     a.append((1,3))
#     a.append((2,4))
#     a.append((3,6))

# if (1,3) in a:
#     print("나이스")

# for i in a:
#     print(i)