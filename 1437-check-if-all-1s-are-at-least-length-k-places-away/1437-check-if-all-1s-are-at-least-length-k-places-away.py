class Solution:
    def kLengthApart(self, nums: List[int], k: int) -> bool:
        num_idx=[idx for idx,val in enumerate(nums) if val==1]
        n=len(num_idx)
        for i in range(n-1):
            if num_idx[i+1]-num_idx[i]-1<k:
                return False
        return True