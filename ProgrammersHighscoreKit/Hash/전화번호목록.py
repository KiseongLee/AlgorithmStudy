# 1차 시도
'''
채점 결과
정확성: 41.7
효율성: 12.5
합계: 54.2 / 100.0
'''
def solution(phone_book):
    answer = True
    phone_book.sort(key=lambda x: len(x))
    for i in range(len(phone_book)):
        for j in range(i+1, len(phone_book)):
            for k in range(len(phone_book[i])):
              if phone_book[i][k] == phone_book[j][k]:
                 answer = False
                 return answer
                    
    return answer

# 2차 시도
'''
채점 결과
정확성: 54.2
효율성: 12.5
합계: 66.7 / 100.0
'''
def solution(phone_book):
    answer = True
    cnt = 0
    phone_book.sort(key=lambda x: len(x))
    for i in range(len(phone_book)):
        for j in range(i+1, len(phone_book)):
            for k in range(len(phone_book[i])):
              if phone_book[i][k] == phone_book[j][k]:
                 cnt += 1
            if cnt == len(phone_book[i]):
                return False
            
    return True

# 3차 시도
'''
채점 결과
정확성: 83.3
효율성: 8.3
합계: 91.7 / 100.0
'''
def solution(phone_book):
    answer = True
    cnt = 0
    phone_book.sort(key=lambda x: len(x))
    for i in range(len(phone_book)):
        for j in range(i+1, len(phone_book)):
            for k in range(len(phone_book[i])):
              if phone_book[i][k] == phone_book[j][k]:
                 cnt += 1
            if cnt == len(phone_book[i]):
                return False
            cnt = 0
            
    return True

# 다른 사람 풀이
'''
index 0이 2의 접두어라면
index 1이 2의 접두어라는 것이 자동적으로 증명이되므로
굳이 다 비교해줄 필요없다.
0은 1과, 1은 2와 비교를 하면서 가면된다.
또한, startswith라는 기본함수 -> string1.startswith(string2)
String1이 String2로 시작되는지 (String2가 String1의 접두어인지)를 찾아주는 기본 함수
'''
def solution(phoneBook):
    phoneBook = sorted(phoneBook)
    for a, b in zip(phoneBook, phoneBook[1:]):
        if b.startswith(a):
            return False
    return True


# hash를 이용한 풀이

def solution(phone_book):
    # 1. Hash map을 만든다
    hash_map = {}
    for phone_number in phone_book:
        hash_map[phone_number] = 1
    # 2. 접두어가 Hash map에 존재하는지 찾는다
    for phone_number in phone_book:
        jubdoo = ""
        for number in phone_number:
            jubdoo += number
            # 3. 접두어를 찾아야 한다 (기존 번호와 같은 경우 제외)
            print(jubdoo)
            if jubdoo in hash_map and jubdoo != phone_number:
                return False
    return True