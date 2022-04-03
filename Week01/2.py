n = int(input())

data=[]
for i in range(n):
    a,b = input().split()
    data.append((a,int(b)))

# 하나는 문자, 하나는 숫자 받기 테크닉

def setting(a):
    return a[1]


data.sort(key=setting)


for i in range(len(data)):
    print(data[i][0], end=' ')
