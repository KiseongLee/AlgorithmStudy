
def solution(lottos, win_nums):

    rank=[6,6,5,4,3,2,1]            # 인덱싱을 통해서 순위를 구하니까 진짜 간단해진다

    cnt_0 = lottos.count(0)
    ans = 0
    for x in win_nums:
        if x in lottos:
            ans += 1
    return rank[cnt_0 + ans],rank[ans]