a, b = input().split()

a_data = []
for i in range(len(a)):
    a_data.append(a[i])
    
b_data = []
for i in range(len(b)):
    b_data.append(b[i])
    
a_data[0], a_data[1], a_data[2] = a_data[2], a_data[1], a_data[0]
b_data[0], b_data[1], b_data[2] = b_data[2], b_data[1], b_data[0]

a = a_data[0] + a_data[1] + a_data[2]
b = b_data[0] + b_data[1] + b_data[2]

a = int(a)
b = int(b)

if a > b:
    print(a)
else:
    print(b)


