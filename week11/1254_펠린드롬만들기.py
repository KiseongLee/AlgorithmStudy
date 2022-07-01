


# value  = -2
# while True:
    
#     for i in range(len(A)):
    
#         if A[i] != A[len(A)-1-i]:
#             A.append(B[value])
#             value -= 1
#             break
        
#     print(i)
    
# from copy import deepcopy


# A = list(input())
# B = deepcopy(A)
# value = -2
# while True:
#     for i in range(len(A)):
      
#         if A[i] != A[-i-1]:
#             A.append(B[value])
#             value -= 1
#             break

  
#     if i == len(A)-1:
#         print(i)
#         print(len(A))
#         break

s = input()

for i in range(len(s)):
    tmp = s + s[:i][::-1]
    # print(s[:i][::-1])
    print(tmp)
    print(i)
    if tmp == tmp[::-1]:
        print(len(tmp))
        break
    