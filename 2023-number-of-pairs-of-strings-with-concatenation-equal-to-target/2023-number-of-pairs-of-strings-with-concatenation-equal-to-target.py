class Solution:
    def numOfPairs(self, nums: List[str], target: str) -> int:
        n=len(target)
        result=0

        for i in range(len(nums)):
            left=nums[i]
            for j in range(len(nums)):
                right=nums[j]
                if i!=j and len(right)==n-len(left) and left+right==target:
                    result+=1
        
        return result