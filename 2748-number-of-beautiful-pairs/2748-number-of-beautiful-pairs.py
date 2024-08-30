class Solution:
    def countBeautifulPairs(self, nums: List[int]) -> int:
        n=len(nums)
        result=0

        for i in range(n-1):
            for j in range(i+1,n):
                if math.gcd(nums[i],nums[j])==1:
                    result+=1
        return result