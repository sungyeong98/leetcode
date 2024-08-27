class Solution:
    def waysToMakeFair(self, nums: List[int]) -> int:
        left_odd,left_even=0,0
        right_odd=sum([val for idx,val in enumerate(nums) if idx%2==1])
        right_even=sum(nums)-right_odd

        result=0
        for idx,val in enumerate(nums):
            if idx==0:
                right_even-=val
            else:
                if idx%2==0:
                    left_odd+=nums[idx-1]
                    right_even-=val
                else:
                    left_even+=nums[idx-1]
                    right_odd-=val

            if left_even+right_odd==left_odd+right_even:
                result+=1
        return result