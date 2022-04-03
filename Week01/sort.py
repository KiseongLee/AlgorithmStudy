from numpy import array_split


data = [9,8,7,6,5,4,2,3,1,0,0,1]

array = [0]*len(data)

for i in range(len(data)):
    array[data[i]] += 1

for i in range(len(array)):
 print(f"{i}"*array[i]) 