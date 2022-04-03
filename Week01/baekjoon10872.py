# def factorial(n):

#     result = 1

#     for i in range(1, n):
#         result *= i
    
#     print(result)
    

# factorial(10)
        
    
def factorial(n):

    if n <= 1 :
        return 1
    
    return n * factorial(n-1)

print(factorial(10))

    
