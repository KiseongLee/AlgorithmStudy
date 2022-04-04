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

# print(operator_permutation)
# print(len(operator_permutation))
# print(operator_permutation[0][0])

total_list=[]
total = number[0]
for i in range(len(operator_permutation)):
     for j in range(len(operator_permutation[i])):
         
         if operator_permutation[i][j] == '+':
             total += number[j+1]
        
         elif operator_permutation[i][j] == '-':
             total -= number[j+1]

         elif operator_permutation[i][j] == '*':
             total *= number[j+1]
        
         elif operator_permutation[i][j] == '/':
             total = int(total/number[j+1])

     total_list.append(total)
     total = number[0]


print(max(total_list))
print(min(total_list))