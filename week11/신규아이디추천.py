# .lower()
#  isalnum, += 
#  .. -> while
# [0](.이 하나 남았을때.), [-1] [1:], [:-1]
# ''이면 a 대입
# 
# 

new_id = "=.="


new_id = new_id.lower() # 1단계

ans = ""                # 2단계
for string in new_id:
    if string.isalnum() or string in '-_.'  :
        ans += string
new_id = ans

while ".." in new_id:   #3단계
    new_id = new_id.replace("..",".") # 갱신해줘야함

if len(new_id) >= 1 and new_id[0] == ".":    #4단계 - 없을때, 예외처리해줘야함!!
    new_id = new_id[1:]
if len(new_id) >= 1 and new_id[-1] == ".":
    new_id = new_id[:-1]

if new_id == "":    #5단계
    new_id = "a"

if len(new_id)>= 16:    #6단계
    new_id = new_id[:15]
if new_id[-1] == ".":
    new_id = new_id[:-1]

if len(new_id)<= 2:     # 7단계
    new_id = new_id + new_id[-1]*(3-len(new_id))
    
print(new_id)