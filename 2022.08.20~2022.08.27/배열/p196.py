# 풀었지만 틀림
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min = -1
        max = 10001
        
        for i in range(len(prices)-1):
            if prices[i] < prices[i+1] and min < 0:
                max = prices[i+1]
                min = prices[i]
                continue
            if min>=0:
                if prices[i] < prices[i+1]:
                    if prices[i+1]>max:
                        max=prices[i+1]
                else:
                    if prices[i+1]<min:
                        min=prices[i+1]
                        
        if min == -1 and max == 10001:
            return 0
        else:
            print(max, min)
            return max-min
# 풀이

