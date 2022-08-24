# my 풀이
class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        count = 0
        X = dict(collections.Counter(jewels))
        Y = dict(collections.Counter(stones))
        Y_key = Y.keys()
        for key, value in X.items():
            if key in Y_key:
                count += Y[key] // value
        return count
    