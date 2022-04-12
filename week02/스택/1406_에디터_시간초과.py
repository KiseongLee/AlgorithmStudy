import sys
input = sys.stdin.readline
stack = list(input().strip())

n = int(input())

edit = []
for i in range(n):
    a = input().strip()
    
    if " " in a:
        a = a.split(" ")
        edit.append(a)
    
    else:
        edit.append(a)
    
point = len(stack)

for i in range(n):
    
    if edit[i] == "L":
        point -= 1
        if point < 0:
            point = 0
    
    if edit[i] == "D":
        point += 1
        if point > len(stack):
            point = len(stack)
    
    if edit[i] == "B":
        if point == 0:
            continue
        stack.pop(point-1)
        point -= 1
       
    
    if edit[i][0] == "P":
        stack.insert(point, edit[i][1])
        point += 1
 
            

print(("".join(stack)))

# pop(i), insert(i)의 시간 복잡도는 O(N)이므로 이 문제를 해결할 떄, 시간복잡도가 O(1)인 list.pop()와 list.append(v)를 이용해야한다.
