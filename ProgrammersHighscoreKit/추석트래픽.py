# 1차 실패.. # 조건도 어려움
from datetime import datetime, timedelta

def solution(lines):
    
    if len(lines) == 1:
        return 1
    
    for i in range(len(lines)):
        a = lines[i].split()
        b = datetime.strptime(a[0]+a[1],'%Y-%m-%d%H:%M:%S.%f')
        c = b - timedelta(seconds=float(a[2][:-1])-0.001)
        lines[i] = [c, b]
    lines.sort()
    t = timedelta(seconds=1)
    
    max_count = 0
    count = 1
    for i in range(len(lines)):
        for j in range(len(lines)):
            if abs(lines[i][0] - lines[j][0]) < t and abs(lines[i][0] - lines[j][1]) < t:
                count += 1
            if max_count < count:
                max_count = count
    
    count = 1
    for i in range(len(lines)):
        for j in range(len(lines)):
            if abs(lines[i][1] - lines[j][0]) < t and abs(lines[i][1] - lines[j][1]) < t:
                count += 1
            if max_count < count:
                max_count = count
 
    return max_count

# 2차 시도
from datetime import datetime, timedelta

def solution(lines):

    if len(lines) == 1:
        return 1

    for i in range(len(lines)):
        a = lines[i].split()
        b = datetime.strptime(a[0]+a[1],'%Y-%m-%d%H:%M:%S.%f')
        c = b - timedelta(seconds=float(a[2][:-1])-0.001)
        lines[i] = [c, b]
    lines.sort()
    t = timedelta(seconds=1)
    zero = timedelta()

    answer =0

    for i in range(len(lines)):
        for j in range(len(lines[i])):
            count = 1
            for k in range(len(lines)):
                if i==k:
                    continue
                b = lines[k][0] - lines[i][j]
                a = lines[k][1] - lines[i][j]
                if (zero <= a and a < t) or (zero <= b and b < t)  or (b < zero and t < a):
                    count += 1
            answer = max(answer, count)


    return answer

# 변형

from datetime import datetime, timedelta


def check(time ,lines):
    t = timedelta(seconds=1)
    count = 0
    start = time
    end = time + t
    for line in lines:
        if line[1] >= start and line[0] < end:
            count += 1
    return count 

def solution(lines):

    if len(lines) == 1:
        return 1

    for i in range(len(lines)):
        a = lines[i].split()
        b = datetime.strptime(a[0]+a[1],'%Y-%m-%d%H:%M:%S.%f')
        c = b - timedelta(seconds=float(a[2][:-1])-0.001)
        lines[i] = [c, b]
    lines.sort()

    answer =0

    for line in lines:
        answer = max(answer, check(line[0], lines), check(line[1], lines))


    return answer

#다른 풀이

def check(time, change):
    count = 0
    start = time
    end = time + 1000  # -1을 안해주는 이유? 구간을 체크할 때 -> 정확히 1초로 계산을 해야한다!!, 시작값은 이미 밑에서 잘 구해놓음
    for c in change:
        if c[1] >= start and c[0] < end:
            count += 1
    return count

def solution(lines):
    
    change =[]
    answer = 1
    for line in lines:
        x,y,z = line.split(" ")     
        a = y.split(":")    
        b = float(z.replace("s",""))*1000   # 구간의 초도 밀리 세컨드로 변환
        end = (int(a[0])*3600+int(a[1])*60 + float(a[2]))*1000 # 시간을 밀리 세컨드로 바꾸기 위해서
        start = end - b + 1 # end값을 구했으니, start값을 구한다.(시작값 포함이므로 +1을 해줬다.)
        change.append([start, end]) # 시작과 끝을 배열에 담는다
    for c in change:
        answer = max(answer, check(c[0], change), check(c[1], change))
    return answer