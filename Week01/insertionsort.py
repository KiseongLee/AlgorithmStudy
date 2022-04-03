
import numpy as np
import time
import datetime


# data = np.random.randint(1,10001,10000)

# start = time.time()

# data = [9,8,7,6,5,4,3,2,1,0]

# for i in range(1, len(data)):
#  for j in range(i, 0, -1):
#     if data[j] < data[j-1]:
#        data[j], data[j-1] = data[j-1], data[j]
#     # else:
#     #     break

# print(data)

# end = time.time()

# sec = end - start
# result = datetime.timedelta(seconds=sec)

# print(result)

data = np.random.randint(1,10001,10000)

start = time.time()

for i in range(1, len(data)):
 for j in range(i, 0, -1):
    if data[j] < data[j-1]:
       data[j], data[j-1] = data[j-1], data[j]
    else:
         break

print(data)

end = time.time()

sec = end - start
result = datetime.timedelta(seconds=sec)

print(result)