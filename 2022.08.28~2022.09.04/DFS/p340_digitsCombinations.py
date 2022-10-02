class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        # 구할 것 : input 번호에 해당하는 문자 조합해서 출력하기
        
        # 문제 풀이 개념 : dfs로 종료 조건 만들어서 풀어내기
        
        # 1. 종료 조건 -> digits와 문자수가 같으면 result에 append
        # 2. for문 돌면서 dfs 실행
        # 3. 호출 : digits를 어떻게 호출 할지?, dict 정의
        
        def dfs(index, path):
            
            if len(path) == len(digits):
                result.append(path)
                return
            
            for i in range(index, len(digits)):
                for j in dict[digits[i]]:
                    dfs(i+1, path+j)
        
        if not digits:
            return []
    
        dict = {"2": "abc", "3": "def", "4": "ghi", "5": "jkl", "6": "mno",
                "7": "pqrs", "8": "tuv", "9": "wxyz"}
        result = []
        dfs(0,"")
        return result
        