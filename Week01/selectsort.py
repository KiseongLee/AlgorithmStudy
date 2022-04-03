
import numpy as np
import time
import datetime


# data = np.random.randint(1,10001,10000)

# start = time.time()

# for i in range(len(data)):
#  for j in range(i+1, len(data)):
#    if data[i] > data[j]:
#       data[i], data[j] = data[j], data[i]
# print(data)

# end = time.time()

# sec = end - start
# result = datetime.timedelta(seconds=sec)

# print(result)

data = np.random.randint(1,10001,100000)

start = time.time()
data.sort()
end = time.time()

sec = end - start
result = datetime.timedelta(seconds=sec)

print(result)