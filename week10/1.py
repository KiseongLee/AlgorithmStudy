from collections import deque


n = 1000

# x1 = deque(str(n))
# x2 = deque(str(n))
# y = x1.popleft()
# z = x2.pop()

# x1.append(y)
# x2.appendleft(z)
# print(x1)
# print(x2)

x1 = deque(str(n))
print(x1)
x1.rotate(1)
print(x1)
x2 = deque(str(n))
x2.rotate(-1)
print(x2)

a=[]
b=[]
for i in range(len(x1)):
    a.append(x1.popleft())
    b.append(x2.popleft())
print(int("".join(a)))
print(int("".join(b)))