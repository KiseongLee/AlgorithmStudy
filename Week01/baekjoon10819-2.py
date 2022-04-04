import itertools
import sys
input = sys.stdin.readline

n = int(input())

number = list(map(int, input().split()))

operator_number = list(map(int, input().split()))

operator = ["+", "-", "*", "/"]

real_operator = []
for i in range(len(operator_number)):

    x = operator[i]

    for i in range(operator_number[i]):
    
        if x != "":
            real_operator.append(x)

operator_permutation = list(itertools.permutations(real_operator, len(real_operator)))

operator_permutation_real = set(operator_permutation)
operator_permutation_real = list(operator_permutation_real)

# print(len(operator_permutation_real))
# result = set(operator_permutation)
# print(len(result))
# print(result)



total_list=[]
total = number[0]
for i in range(len(operator_permutation_real)):
     for j in range(len(operator_permutation_real[i])):
         
         if operator_permutation_real[i][j] == '+':
             total += number[j+1]
        
         elif operator_permutation_real[i][j] == '-':
             total -= number[j+1]

         elif operator_permutation_real[i][j] == '*':
             total *= number[j+1]
        
         elif operator_permutation_real[i][j] == '/':
             total = int(total/number[j+1])

     total_list.append(total)
     total = number[0]


print(max(total_list))
print(min(total_list))