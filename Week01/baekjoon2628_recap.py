r,c = map(int, input().split())

row = [0]
column = [0]

x = int(input())

for i in range(x):
    a, b = map(int, input().split())

    if a == 0:
            column.append(b)
    elif a == 1:
            row.append(b)
    
column.sort()
row.sort()

row.append(r)
column.append(c)

max_c = -1 
max_r = -1
for i in range(len(row)-1):
    if max_r < row[i+1] - row[i]:
       max_r = row[i+1] - row[i]

for i in range(len(column)-1):
    if max_c < column[i+1] - column[i]:
        max_c = column[i+1] - column[i]

print(max_r*max_c)