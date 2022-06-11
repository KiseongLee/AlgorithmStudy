from itertools import permutations

def check(users, banned_id):
    
    for i in range(len(banned_id)):
        
        
        if len(banned_id[i]) != len(users[i]): # 이게 핵심이네요 i를 갖게 놓는 것
            return False                       # 내가 생각한건 하나씩 다 검색해줘야 하는거 아니야 했지만
                                               # 조건을 생각해보면 하나가 같지 않으면 바로 False 해버리면 되고
                                               # 맞으면 바로 넘어가면 되니까 이렇게 하면되고
        for j in range(len(users[i])):
            
            if banned_id[i][j] == "*":
                continue
            if banned_id[i][j] != users[i][j]:
                return False

    return True


def solution(user_id, banned_id):
    user_permutation = list(permutations(user_id, len(banned_id)))
    banned_Set =[]
    
    for users in user_permutation:
        
        if not check(users, banned_id):
            continue
    
        else:
            users = set(users)      # 튜플로 set할 수 있는 것이고 permutation돌리면 tuple로 나오는 구나!
            if users not in banned_Set: # 중복이 담기지 않게 넣어주면 (순서는 상관 없어버림)
                banned_Set.append(users)
    
    
    return len(banned_Set)


'''
안보고 풀어봤음
1. 체크하는 함수 만드는 데 거기서 i를 갖게 놓는 것 -> 되면 같이 넘어가는 거지(하나씩 다 해보는게 아니라)
2. set -> 체크했고 False들 다거른다음, 순서는 다른데 반복되는 것이 있을거야, 이걸 제거해줘야하는거지
3. 그리고 담으면되는데 -> 당연히 not in 걸면 되겠다.
def check(users, banned_id):
    
    for i in range(len(banned_id)):
        
        if len(users[i]) != len(banned_id[i]):
            return False
        
        for j in range(len(users[i])):
            
            if banned_id[i][j] == "*" or banned_id[i][j] == users[i][j]:
                continue
            else:
                return False
    
    return True
    
    

def solution(user_id, banned_id):
    
    user_id_permu = list(permutations(user_id, len(banned_id)))
    banned_set =[]
    
    for users in user_id_permu:
        
        if not check(users, banned_id):
            continue
        
        else:
            users = set(users)
            if users not in banned_set:
                banned_set.append(users)
    
    return len(banned_set)

user_id =["frodo", "fradi", "crodo", "abc123", "frodoc"]
banned_id =["fr*d*", "*rodo", "******", "******"]

solution(user_id, banned_id)

'''