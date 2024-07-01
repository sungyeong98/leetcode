from itertools import combinations
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result=[nums]
        for i in range(len(nums)):
            for j in combinations(nums,i):
                result.append(list(j))
        return result