n = int(input())

honey = list(map(int, input().split()))

sum1 = []
sum1_value = 0
for i in range(n-2, 0, -1):
    for j in range(i):
        sum1_value += honey[j]
    
    sum1.append(sum1_value)
    sum1_value = 0

sum2 = []
sum2_value = 0
for i in range(n-2, 0, -1):
    for j in range(n-1):
        if i != j:
            sum2_value += honey[j]
    
    sum2.append(sum2_value)
    sum2_value = 0

sum3 = [sum1[i] + sum2[i] for i in range(len(sum1))]
max_value = max(sum3)

sum1=[]
sum2=[]
sum1_value =0
sum2_value =0
for i in range(2, n):
    for j in range(i, n):
        sum1_value += honey[j]
    sum1.append(sum1_value)
    sum1_value = 0
for i in range(1, n-1):
    for j in range(1,n):
        if i != j:
            sum2_value += honey[j]
    sum2.append(sum2_value)
    sum2_value
sum3 = [sum1[i] + sum2[i] for i in range(len(sum1))]
X = max(sum3)

if max_value < X:
    max_value = X


if n % 2 != 0:
   x = (n//2 + 1) -1
   
   x_value = 0
   for i in range(1,x+1):
       x_value += honey[i]
   for i in range(n-2, x-1 ,-1):
       x_value += honey[i]
    
   if max_value < x_value:
      max_value = x_value

print(max_value)
   
    
