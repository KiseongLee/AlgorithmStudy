# 문자열 관련 구현 문제
# 알파벳을 탐색하면서 단축키를 지정해야함
# 단축키를 탐색하면서 없으면 바로 리스트에 넣었음
# 단축키에 있으면 다음 단어를 가지고 찾아보고 또 없으면 맨앞에서부터 보면서 없는 값을 단축키로 지정해야함

# 1. 띄어쓰기가 있는 단어 구분 -> 2가지로 분리해서 생각
# 2. 단어 탐색을 하면서 단축키가 있는 경우 -> 1) 다음 단어가 있는 경우 -> 그 다음 단어의 첫 값만 비교
#                                                           없으면 하나씩 탐색하면서 단축키에 있는지 비교 
#                                    2) 다음 단어가 없는 경우 -> 하나씩 탐색하면서 단축키에 있는지 비교
# 3. 출력할 때, 대괄호 양쪽에 넣는 방법

# 생각해야할 조건도 많았지만, 출력할 때, 대괄호 양쪽에 넣는 방법도 몰랐다.


# n = int(input())

# data = []
# for i in range(n):
#     data.append(input())

# vocabul = []
# shortkey = []
# ans = []

# for voca in data:
   
#    if " " in  voca:
#      voca2 = list(voca.split(' '))
#      for x in voca2:
#         if not x in vocabul:
#             vocabul.append(x)
#             for i in range(len(x)):
#                 if not x[i] in shortkey:
#                    shortkey.append(x[i])
#                    break
               
       
       
#    else:
#     if not voca in vocabul:
#       vocabul.append(voca)
#       for i in range(len(voca)):
#         if not voca[i] in shortkey:    
#            shortkey.append(voca[i])
#            break 
          

# print(shortkey)
n = int(input())
dList = []

def plus(c):

    if c.isupper():
      dList.append(c)
      dList.append(c.lower())
    
    else:
      dList.append(c)
      dList.append(c.upper())
      
for i in range(n):
  sList = list(input().rstrip().split(' '))
  flag = False
  for j in range(len(sList)):
    if sList[j][0] not in dList: #단축키 설정 가능
       plus(sList[j][0])
       temp = sList[j][0]
       sList[j] = sList[j][1:]
       sList[j] = '[' + temp + ']' + sList[j]
       flag = True
       break
  if flag:
       print(' '.join(sList))
       continue
  for j in range(len(sList)):
      flag = False
      for k in range(len(sList[j])):
        if sList[j][k] not in dList:
            plus(sList[j][k])
            temp = sList[j][k]
            if k != len(sList[j])-1:
              sList[j] = sList[j][:k] + '['+temp+']'+sList[j][k+1:]
            else:
              sList[j] = sList[j][:k] + '[' + temp + ']'
            flag = True
            break
      if flag:
         break
  print(' '.join(sList))