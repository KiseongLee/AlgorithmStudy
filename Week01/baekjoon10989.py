import sys

input = sys.stdin.readline

n = int(input())
data = [0]*10001

for i in range(n):
    data[int(input())] += 1


for i in range(len(data)):
    if data[i] != 0:
        for j in range(data[i]):
            print(i)