class Solution:
    def maxDivScore(self, nums: List[int], divisors: List[int]) -> int:
        temp=[]
        divisors.sort()
        for i in divisors:
            cnt=0
            for j in nums:
                if j%i==0:
                    cnt+=1
            temp.append(cnt)
        return divisors[temp.index(max(temp))]