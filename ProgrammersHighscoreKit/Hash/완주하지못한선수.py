# def solution(participant, completion):
    
#     ans = []
#     for i in range(len(participant)):
#         if participant[i] in completion and not participant[i] in ans:
#             ans.append(participant[i])

#     for i in range(len(ans)):
#         if ans[i] in participant:
#             participant.remove(ans[i])
    
#     for i in range(len(participant)):
#         answer = f"{participant[i]}"
#     return answer


# def solution(participant, completion):

#     for p in participant:
#         if participant.count(p) > completion.count(p):
#             return p

# sort를 이용한 풀이 (zip 사용 방법 알아두기)
def solution(participant, completion):
    participant.sort()
    completion.sort()
    for p, c in zip(participant, completion):
        if p != c:
            return p
    return participant.pop()



# collections.Counter를 이용한 풀이 -> 빼기가 가능
participant = ["marina", "josipa", "nikola", "vinko", "filipa"]	
completion = ["josipa", "filipa", "marina", "nikola"]

import collections

def solution(participant, completion):
    answer = collections.Counter(participant) - collections.Counter(completion)

    return list(answer.keys())[0]

print(solution(participant, completion))