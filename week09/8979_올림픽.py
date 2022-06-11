
# nations ={}
# for _ in range(n):
#     X = list(map(int, input().split(' ')))
#     key = X[0]
#     X.pop(0)
#     for i in range(len(X)):
#         value = X[i]
#         nations[key].add(value)

# print(nations)    
# nations = sorted(nations.items(), key=lambda x: (-x[0],-x[1],-x[2]))

# print(nations)
    
# n, k= map(int, input().split())
    

# nations=[]
# for i in range(n):
#     nations.append(list(map(int, input().split())))


# nations = sorted(nations, key=lambda x: (x[1],x[2],x[3]))

# s = 0
# for i in range(len(nations)):
    
#     if nations[i][3] == k:
        
#        if i <= len(nations)-2:
    
#          if nations[i][0:3] == nations[i+1][0:3]:
#              s += 1
#              continue
#          else:
#              if s:
#                  print(nations[i][3])       
    
#     if i == len(nations)-1:
#             print(nations[i][3])

# print(nations)



n, k= map(int, input().split())
    
nations=[]
for i in range(n):
    nations.append(list(map(int, input().split())))

nations.sort(key=lambda x: (x[1],x[2],x[3]), reverse = True)

grade, s = 1, 0
for i in range(n):
    if i != 0:
        if nations[i-1][1:] == nations[i][1:]:
            s += 1
        else:
            if s:
                grade += s
                s = 0
            grade += 1
    if nations[i][0] == k:
        print(grade)
        break