n, S = map(int, input().split())

array = list(map(int, input().split()))

count = 0
sum = 0

def com(value, idx):
    global count, sum
    
   
    for i in range(len(array)):
         if idx < i:

            sum += array[i]
            if sum == S:
                count += 1
            com(value+array[i], i)
            sum -= array[i]



com(0, -1)
print(count)