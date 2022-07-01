# 이중 포문은 아닌듯
# 투포인터로 풀어야할듯
# 시간초과, 효율성 0점

# def solution(gems):
#     answer = []
#     a = set(gems)
#     x = list(a)
#     for i in range(len(gems)-len(x)+1):
#       for j in range(len(gems) - (len(x)+i)+1):
#           y = gems[j:j+(len(x)+i)]
#           b = set(y)
          
#           if a==b:
#              return [j+1,j+(len(x)+i)]



# def solution(gems):
#     answer = []
#     a = set(gems)
#     x = list(a)
        
#     for start in range(len(gems)):
#         for end in range(len(x)+start, len(gems)+1):
     
#             if a == set(gems[start:end]):
#                answer.append([start+1, end])
                
#     min_value = 1e9
#     answer2 = []
#     for i in range(len(answer)):
#       if min_value >= abs(answer[i][0] - answer[i][1]):
#             min_value = abs(answer[i][0] - answer[i][1])
            
#     for i in range(len(answer)):
#         if answer[i][1] - answer[i][0] == min_value:
#             answer2.append([answer[i][0], answer[i][1]])
           
    
#     return answer2[0]



'''
gems 길이 = n
kind = gems의 종류
answer는 처음과 끝
dic 정의 -> 종류를 체크해야하기 때문에 (일단 첫값 넣어놓기)
s,e = 0, 0(투포인터 사용)

반복문 시작 -> 조건은 s와 e가 N보다 작으면 도는 것이고
    if : 종류가 딕셔너리 길이보다 작으면 (더 추가해줘야하면)
         끝값을 늘리고
        만약에 endpoint가 끝값이 되면 브레이크(end=n)
        dic값 갱신
    
    else:
        answer 갱신을 위한 조건
        dic[key] == 1이면 del 
        아니면 value를 빼주고
        start값을 올려주면됨

answer 0 1
answer 1 1
        
'''