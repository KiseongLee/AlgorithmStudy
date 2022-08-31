# 내 풀이
def solution(arr):
    answer = []
    for i in arr:
        if not answer:
            answer.append(i)
            continue
        if answer[-1] != i:
            answer.append(i)
    return answer



# 내 생각 좋은 풀이
def no_continuous(s):
    a = []
    for i in s:
        if a[-1:] == [i]: continue
        a.append(i)
    return a