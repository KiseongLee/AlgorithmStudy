# https://programmers.co.kr/learn/courses/30/lessons/86051

numbers=list(map(int, input().split()))
number = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

sum = 0
for x in number:
    if x in numbers:
        continue
    sum += x

print(sum)