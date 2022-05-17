# def solution(id_list, report, k):
#     stop = []
#     report_dic = {id: [] for id in id_list}
#     for i in set(report):
#         rep = i.split(' ')
#         stop.append(rep[1])
#         report_dic[rep[0]].append(rep[1])
#     stop = set([i for i in stop if stop.count(i) >= k])
    
#     for key, value in report_dic.items():
#         for s in stop:
#             if s in value :
#                 answer[id_list.index(key)] += 1
#     return answer

# id_list = list(map(str, input().split()))
# answer = [0] * len(id_list)

# stop = []
# report_dic = {id: [] for id in id_list }
# for i in set(report):
#     rep = i.split(' ')


from collections import defaultdict


def solution(id_list, report, k):
    answer = []
    
    report_to_from = defaultdict(set)
    report_from_to = defaultdict(set)
    for r in report:
        report_from, report_to = r.split(' ')
        report_to_from[report_to].add(report_from)
        report_from_to[report_from].add(report_to)
    
    for _id in id_list:
        cnt = 0
        for r_to in report_from_to[_id]:
            if len(report_to_from[r_to]) >= k:
                cnt += 1
        answer.append(cnt)
    return answer
    


