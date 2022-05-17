t = int(input())

for _ in range(t):
    
    n = int(input())
    score = []
    for i in range(n):
        a, b = map(int, input().split())
        score.append((a,b))
    score.sort()
    
    X = score[0][1]
    count = 1
    for i in range(1, len(score)):
        if X > score[i][1]:
            count += 1
            X = score[i][1]
    print(count)
            
       