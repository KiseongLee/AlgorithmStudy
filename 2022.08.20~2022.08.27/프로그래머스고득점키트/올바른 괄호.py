# 파이썬 알고리즘 책의 풀이
def solution(s):
    stack = []
    table = { ")" : "("}
    
    for char in s:
        if char not in table:
            stack.append(char)
        elif not stack or table[char] != stack.pop():
            return False
        
    return len(stack) == 0

# 나의 풀이
def solution(s):
    stack = []
    table = {')':'('}
    for i in s:
        if i not in table:
            stack.append(i)
            continue
        if stack:
            stack.pop()
            continue
        if len(stack) == 0 and i == ")":
            return False
    if stack:
        return False
    return True

# 내 생각에 좋은 풀이
def is_pair(s):
    st = list()
    for c in s:
        if c == '(':
            st.append(c)

        if c == ')':
            try:
                st.pop()
            except IndexError:
                return False

    return len(st) == 0