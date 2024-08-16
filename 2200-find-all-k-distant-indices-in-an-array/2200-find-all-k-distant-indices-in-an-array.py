class Solution:
    def findKDistantIndices(self, nums: List[int], key: int, k: int) -> List[int]:
        result=[]
        n=len(nums)
        target=[idx for idx,val in enumerate(nums) if val==key]

        for i in range(n):
            if i in target:
                result.append(i)
                continue
            for j in target:
                if abs(i-j)<=k:
                    result.append(i)
                    break
        
        return result