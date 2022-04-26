# n, k = map(int, input().split())

# data = list(map(int, input().split()))

# result = []
# cnt = 0

# for i in range(k):
    
#     if len(result)+1 <= n and not data[i] in result:
#         result.append(data[i])

#     elif not data[i] in result:
#          result.pop()
#          result.append(data[i])
#          cnt += 1

# print(cnt)




from sys import stdin
input = stdin.readline
N, K = map(int,input().split())
things = list(map(int,input().split()))
pluged = set()
cnt = 0
for idx, thing in enumerate(things) :
    # idx = 물건 index, thing = 물건 값
    if thing in pluged :
        # pluged에 thing이 있으면(이미 있는 것 이면)
        continue
    
    if len(pluged) < N :
        # pluged의 길이가 N보다 작으면
        pluged.add(thing)
        # pluged에 thing을 append 해준다
        continue
    
    temp = (0, 0)
        # temp는 0,0 튜플로 받는다
    for p in pluged :
        # pluged에 꽂혀있는 것들을 확인한다.
        if p not in things[idx:] :
            # things의 idx(현재 꽂혀있는 것) 기준으로 뒤에 꽂혀있는 것(p)가 없다면
            temp = (p,)
            # temp에 p를 넣고 break한다.
            break
        found = things[idx:].index(p)
        # things에 p가 있으면, p값의 index값을 things에서 찾은다음 found라는 변수에 넣어준다.
        if temp[1] < found :
            # temp[1]이 found가 더 크면 (index가 앞에 있는 것은 뒤에 있는 것과 비교했을 때, 뒤에 있는 것을 바꿔줘야한다.)
            # 앞에 있는 것을 바꾸면 번거롭다. 뒤에 있는 것을 또 갈아끼워줘야하므로 손해를 본다.
            temp = (p, found)
            # temp는 (p, found)로 갱신한다.
    pluged.discard(temp[0])
    pluged.add(thing)
    cnt += 1
print(cnt)

