c = int(input())

for _ in range(c):
    data = list(map(int, input().split()))

    n = data[0]
    del data[0]

    sum = 0
    count = 0
    for i in range(n):
        sum += data[i]

    average = sum / n

    for j in range(n):
        if data[j] > average:
            count += 1
        
    percent = (count / n)*100
    print("%0.3f%%" % percent)


    
