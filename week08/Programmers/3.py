# https://programmers.co.kr/learn/courses/30/lessons/76501

sum=0
for i in range(len(absolutes)):
    if signs[i] == True:
        sum += absolutes[i]
    else:
        sum -= absolutes[i]