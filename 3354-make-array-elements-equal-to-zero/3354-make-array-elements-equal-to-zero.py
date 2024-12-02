class Solution:
    def countValidSelections(self, nums: List[int]) -> int:
        n, result = len(nums), 0
        left, right = [0 for _ in range(n)], [0 for _ in range(n)]
        for i in range(1,n):
            left[i]=left[i-1]+nums[i-1]
            right[-i-1]=right[-i]+nums[-i]
        for idx, num in enumerate(nums):
            if num!=0:
                continue
            if left[idx]==right[idx]:
                result+=2
            if abs(left[idx]-right[idx])==1:
                result+=1
        return result