problem = list(map(str, input().split('-')))

ans = 0

if len(problem) == 1:
   x = list(map(int, problem[0].split('+')))
   ans = sum(x)
   print(ans)
else:
    sum2 = 0
    x = list(map(int, problem[0].split("+")))
    ans = sum(x)
    for i in range(1, len(problem)):
        y = list(map(int, problem[i].split('+')))
        sum2 += sum(y)
    print(ans-sum2)