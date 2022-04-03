from itertools import combinations

data = []
for i in range(9):
    data.append(int(input()))

data_a =[]
for i in combinations(data, 7):
    data_a.append(i)

for i in range(len(data_a)):
  
  if sum(data_a[i]) == 100:
    
    data_a_list = list(data_a[i])
    data_a_list.sort()

    for j in data_a_list:
       print(j)
    break
        
       
