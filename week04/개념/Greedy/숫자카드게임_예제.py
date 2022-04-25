# n, m = map(int, input().split())

# data = [list(map(int, input().split())) for i in range(n)]

# for i in range(len(data)):
#     data[i].sort()
    
# max_value = 0

# for i in range(len(data)):
#     if max_value < data[i][0]:
#         max_value = data[i][0]

# print(max_value)



n, m = map(int, input().split())

max_value =0
for i in range(n):
    data = list(map(int,input().split()))
    
    min_value = min(data)
    
    max_value = max(max_value, min_value)

print(max_value)