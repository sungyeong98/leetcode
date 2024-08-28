class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        target=set(range(1,k+1))
        temp, cnt = set(), 0
        while nums:
            cnt+=1
            if nums[-1]<=k:
                temp.add(nums.pop())
            else:
                nums.pop()
            if temp==target:
                break
        return cnt