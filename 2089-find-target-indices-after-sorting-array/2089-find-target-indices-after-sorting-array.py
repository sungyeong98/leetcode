class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        nums.sort()
        result=[]
        cnt=0
        for i in nums:
            if i==target:
                result.append(cnt)
            cnt+=1
        return result