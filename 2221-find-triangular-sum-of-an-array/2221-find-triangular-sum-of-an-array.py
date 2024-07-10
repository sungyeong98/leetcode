from collections import deque
class Solution:
    def triangularSum(self, nums: List[int]) -> int:
        if len(nums)==1:    return nums[0]
        n,nums=len(nums),deque(nums)
        cnt=sum([i for i in range(1,n+1)])

        while cnt>=0:
            n1,n2=nums.popleft(),nums[0]
            num=(n1+n2)%10

            nums.append(num)
            cnt-=1
        return nums.popleft()