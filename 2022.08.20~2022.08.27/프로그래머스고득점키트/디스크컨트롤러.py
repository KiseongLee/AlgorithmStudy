# 핵심은 시간이 적게 걸리는 것부터 처리해야한다는 것 그래서 heapq를 쓸 수 있다.
import heapq
def solution(jobs):
    # 답, 현재 시간, 인덱스
    answer, now, i = 0, 0, 0
    # 처리되는 것 시작값 정의
    start = -1
    heap = []
    #처리되는 것(jobs에 있는 것)들이 다 되면 반복문 탈출
    while i < len(jobs):
        for j in range(len(jobs)):
            if start<jobs[j][0]<=now:
                heapq.heappush(heap, [jobs[j][1],jobs[j][0]])
        if heap:
            x = heapq.heappop(heap)
            start = now
            now = start + x[0]
            answer += now - x[1]
            i += 1
        else:
            now += 1
    return answer//len(jobs)