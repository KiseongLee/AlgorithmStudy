
# 3차 시도 만에 품
# 1. hash_map_list.sort에서 내림차순으로 정렬안함
# 2. answer.append(total_list[j+1][1]) -> j+1이 없을 때 고려를 안함
# 3. j+1이 범위가 넘어갈 때 고려를 안함

def solution(genres, plays):
    answer = []
    hash_map = {}
    for i in range(len(genres)):
        if genres[i] in hash_map:
            hash_map[genres[i]] += plays[i]
        else:
            hash_map[genres[i]] = plays[i]
    hash_map_list = list(hash_map.items())
    hash_map_list.sort(key=lambda x: (-x[1]))
    print(hash_map_list)
    total_list =[]
    for i in range(len(genres)):
        total_list.append((genres[i], i, plays[i]))
    total_list.sort(key=lambda x: (x[0], -x[2], x[1]))
    print(total_list)
    for i in range(len(hash_map_list)):
        for j in range(len(total_list)):
            if hash_map_list[i][0] == total_list[j][0]:
                    answer.append(total_list[j][1])
                    if j <= len(total_list)-2 and hash_map_list[i][0] == total_list[j+1][0]:
                        answer.append(total_list[j+1][1])
                        break
    print(answer)
        
    
    return answer
