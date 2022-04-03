# import sys

# a, b = map(int, sys.stdin.readline().split())

# n = int(input())

# max_real_b = 0
# max_real_a = 0
# max_b = 0
# max_a = 0
# for i in range(n):
#     c, d = map(int, sys.stdin.readline().split())



#     if c == 0:
#         if d >= b/2:
#             max_b = d
#         else: 
#             max_b = b-d
        
    
#         if max_b > max_real_b:
#             max_real_b = max_b
#         print(max_real_b)
    
#     if c == 1:
#         if d >= a/2:
#             max_a = d
#         else:
#             max_a = a-d
        
    
#         if max_a > max_real_a:
#             max_real_a = max_a
#         print(max_real_a)

# print(max_real_a * max_real_b)

import sys
a, b = map(int, sys.stdin.readline().split())
n = int(input())

row = [0]
column = [0]

for i in range(n):
    c, d = map(int, sys.stdin.readline().split())

    if c == 0:
        column.append(d)


    elif c==1:
        row.append(d)

row.append(a)
column.append(b)

row.sort()
column.sort()

max_a = 0
max_b = 0
max_column = 0
max_row = 0

for i in range(len(column)-1):
    max_b = column[i+1]-column[i]
    if max_b > max_column:
        max_column = max_b

for i in range(len(row)-1):
    max_a = row[i+1]-row[i]
    if max_a > max_row:
        max_row = max_a

print(max_column*max_row)