class Solution:
    def countBeautifulPairs(self, nums: List[int]) -> int:
        n=len(nums)
        result=0

        for i in range(n-1):
            n1=int(str(nums[i])[0])
            for j in range(i+1,n):
                n2=int(str(nums[j])[-1])
                if math.gcd(n1,n2)==1:
                    result+=1
        return result