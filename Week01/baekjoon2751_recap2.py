
def merge_sort(arr):
    
   if len(arr) < 2 :
       return arr
   
   mid = len(arr)//2
   low_arr = merge_sort(arr[:mid])
   high_arr = merge_sort(arr[mid:])
   
   merge_arr=[]
   l = h = 0
   
   while l < len(low_arr) and h < len(high_arr):
       
       if low_arr[l] < high_arr[h]:
           merge_arr.append(low_arr[l])
           l += 1
       else:
           merge_arr.append(high_arr[h])
           h += 1
    
   merge_arr += low_arr[l:]
   merge_arr += high_arr[h:]
   return merge_arr

n = int(input())

arr = []
for i in range(n):
    arr.append(int(input()))

result = merge_sort(arr)

for i in range(n):
    print(result[i])
