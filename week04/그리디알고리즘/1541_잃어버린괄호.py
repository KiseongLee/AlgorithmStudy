import sys
input = sys.stdin.readline

data = list(input().rstrip().split('-'))

ans=[]
if len(data) == 1:
    result = list(map(int, data[0].split('+')))
    print(sum(result))

else:
    first_value = list(map(int, data[0].split('+')))
    first = sum(first_value)
    for i in range(1, len(data)):
        result = list(map(int, data[i].split('+')))
        ans.append(sum(result))
    print(first - sum(ans))


