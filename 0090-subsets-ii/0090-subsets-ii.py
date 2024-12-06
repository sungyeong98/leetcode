class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        result, temp = [], []
        n = len(nums)
        nums.sort()

        def helper(idx):
            if n<=idx:
                result.append(temp[:])
                return
            
            temp.append(nums[idx])
            helper(idx+1)
            temp.pop()

            while idx+1<n and nums[idx]==nums[idx+1]:
                idx+=1
            
            helper(idx+1)
        
        helper(0)
        return result