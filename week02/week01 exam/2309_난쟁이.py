array = []
for i in range(9):
    array.append(int(input()))


visited =[]
count = 0
sum = 0
def com(value, idx):
    global count, sum
    
    if len(visited) == 7:
        if sum == 100:
            
            # print(visited)
            visited.sort()
            for j in range(7):
                print(visited[j])
            exit()
           
    
   
    for i in range(len(array)):
         if idx < i:
            visited.append(array[i])
            sum += array[i]
            # print(visited)
            com(value+array[i], i)
            sum -= array[i]
            visited.pop()


com(0, -1)


# 디버깅 포인트 : 어차피 100이 되는 것 하나만 걸리면 출력하면 되기 때문에 바로 함수를 나가주면된다. 
#               근데 return으로 하면 이게 재귀함수이기 때문에  sum == 100되는 경우의 함수만 나가게 된다.
#               그래서 함수 강제 종료가 필요한데 그게 exit()이다. 하나 배웠다.