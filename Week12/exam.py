# a = {{2},{2,1},{2,1,3},{2,1,3,4}}

a = "{{1,2,3},{2,1},{1,2,4,3},{2}}"	

c = a[2:-2]
d = c.split("},{")


for i in range(len(d)):
    d[i]=list(map(int, d[i].split(",")))
    
d.sort(key=lambda i:len(i))


b = []
for i in range(len(d)):
    for j in range(len(d[i])):
        if d[i][j] not in b:
            b.append(d[i][j])
print(b)


# def solution(s):
    
#     c = s[2:-2]
#     d = c.split("},{")


#     for i in range(len(d)):
#         d[i]=list(map(int, d[i].split(",")))
    
#     d.sort(key=lambda i:len(i))


#     b = []
#     b_set = set(b)
#     for i in range(len(d)):
#         for j in range(len(d[i])):
#             if d[i][j] not in b_set:
#                 b.append(d[i][j])
#                 b_set.add(d[i][j])
#                 break
#     return b

'''
집합에 집합을 못넣는 이유?
집합 안에는 무조건 바뀌지 않는 key(immutable)가 들어와야하기 때문에
'''