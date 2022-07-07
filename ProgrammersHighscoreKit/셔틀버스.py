def solution(n, t, m, timetable):
    
    crewtime = [int(time[:2])*60 + int(time[3:]) for time in timetable]
    crewtime.sort()
    bus_time = [540 + t*i for i in range(n)]  
    
    i = 0       # 다음에 버스에 오를 크루의 인덱스
    for tm in bus_time:
      cnt = 0   # 버스에 타는 크루 수
      while cnt < m and i < len(crewtime) and crewtime[i] <= tm:
        i += 1
        cnt += 1
      # 버스에 자리가 남았을 경우
      if cnt < m: 
        answer = tm
      # 버스에 자리가 없는 경우 맨 마지막 크루보다 1분 먼저 도착
      else: 
        answer = crewtime[i-1]-1

    return str(answer//60).zfill(2) + ":" + str(answer%60).zfill(2)

    return answer
