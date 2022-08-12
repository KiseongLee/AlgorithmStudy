count = int(input())
sum_list = input()

sum_list_int = list(sum_list)

sum_total = 0
for i in sum_list_int:
    i_int = int(i)
    sum_total += i_int 

print(sum_total)