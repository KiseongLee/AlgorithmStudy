n = int(input())

count = 0
for i in range(1, n+1):
    
    if i <= 99:
        count += 1

    else:
        a = list(map(int, str(i)))
        
        if a[2] - a[1] == a[1] - a[0]:
             count += 1
       
print(count)