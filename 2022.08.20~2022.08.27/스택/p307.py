# class Solution:
#     def topKFrequent(self, nums: List[int], k: int) -> List[int]:
#         result=[]
#         X = collections.Counter(nums)
        
#         for i in X.most_common(k):
#             result.append(i[0])
#         return result


A = [(1,2),(3,4),(5,6),(7,8),(9,10),(11,12)]
print(list(zip(*A)))