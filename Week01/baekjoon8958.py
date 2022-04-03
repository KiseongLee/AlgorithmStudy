t = int(input())

score = 0
sum = 0
for i in range(t):
    a = input()

    for i in range(len(a)):
        if a[i] == 'O':
            score += 1
            sum += score
        
        else:
            score = 0
    print(sum)
    score = 0
    sum = 0
