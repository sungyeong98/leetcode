class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        result=set()

        for i in range(len(nums)):
            for j in range(i+1, len(nums)+1):
                result.add(tuple(nums[i:j]))
        
        result = list(result)
        result.append([])

        return result