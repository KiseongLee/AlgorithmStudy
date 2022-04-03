import numpy as np
import time
import datetime


# data = [9,8,7,6,5,4,2,3,1,0]

data = np.random.randint(1,10001,10000)

def quick_sort(data, start, end):

    if start >= end :
        return

    pivot = start
    left = start + 1
    right = end

    while left <= right:

        while left <= end and data[left] <= data[pivot]:
            left += 1

        while right > start and data[right] >= data[pivot]:
            right -=1
        
        if left > right:
            data[pivot], data[right] = data[right], data[pivot]
        
        else:
            data[left], data[right] = data[right], data[left]
    
    quick_sort(data, start, right-1)
    quick_sort(data, right+1, end)


start = time.time()

quick_sort(data, 0, len(data)-1)

end = time.time()

sec = end - start
result = datetime.timedelta(seconds=sec)

print(result)
print(data)
