n = int(input())


value = 665
count = 0
while True:
    
    if n == count:
        print(value)
        break
    
    value += 1
    value = str(value)
    
    if '666' in value:
        count += 1
    
    value = int(value)
    

# 15분걸림
# 정말 간단한 문제고, 다 셀 필요없이, 그냥 문자열로 접근하면 정말 쉽다.
# 규칙 찾아내다가 이건 아닌거 같은데 생각 하고 돌려서 생각하니 금방풀림.