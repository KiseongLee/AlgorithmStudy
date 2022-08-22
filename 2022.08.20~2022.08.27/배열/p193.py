#Timeout
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        result = []
        for i in range(len(nums)):
            result_value = 1
            for j in range(len(nums)):
                if i == j:
                    continue
                else:
                    result_value *= nums[j]
            result.append(result_value)
        return result   
#풀이 -> 왼쪽곱, 오른쪽곱

out = []
p = 1
for i in range(len(nums)):
    out.append(p)
    p = p * nums[i]

p = 1
for i in range(len(nums), -1, -1):
    out[i] = out[i] * p
    p = p * nums[i]

return out