def removeDuplicateLetters(s):
    for char in sorted(set(s)):
        suffix = s[s.index(char):]
        print(suffix)
        print(set(s), 1)
        print(set(suffix), 2)

s = "cbacdcbc"
removeDuplicateLetters(s)

'''
1. set를 이용해 사용한 알파벳을 구한다.
2. Counter를 사용해 사용된 알파벳마다 사용된 갯수를 구한다.
3. 문자열의 모든 문자를 반복하며 Counter값을 줄여나가고 Stack에 문자가 없으면 문자를 삽입하고
   있다면 다음 문자로 넘어간다.
   - 스택에 넣기 전에 현재 문자가 앞에 쌓인 문자보다 사전식으로 앞선다면 앞에 쌓인 문자가 뒤에도 있는지 확인하고 뒤에도 있다면 쌓인 문자를 빼고 없다면 그대로 두고 현재 문자를 삽입한다.
'''