class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n=len(nums)
        save={}
        result=[]
        for i in range(n):
            left=nums[:i]
            right=nums[i+1:]
            mul=1
            if left:
                left.sort()
                if tuple(left) not in save:
                    save[tuple(left)]=reduce(operator.mul, left, 1)
                mul*=save[tuple(left)]
            if right:
                right.sort()
                if tuple(right) not in save:
                    save[tuple(right)]=reduce(operator.mul, right,1)
                mul*=save[tuple(right)]
            result.append(mul)
        return result