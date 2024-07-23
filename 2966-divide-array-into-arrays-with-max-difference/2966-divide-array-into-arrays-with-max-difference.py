class Solution:
    def divideArray(self, nums: List[int], k: int) -> List[List[int]]:
        n=len(nums)
        nums.sort()

        temp=[[j for j in nums[i:i+3]] for i in range(0,n,3)]

        for i in temp:
            if max(i)-min(i)>k:
                return []
        return temp