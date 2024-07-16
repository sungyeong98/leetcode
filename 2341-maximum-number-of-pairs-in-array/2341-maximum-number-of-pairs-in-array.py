class Solution:
    def numberOfPairs(self, nums: List[int]) -> List[int]:
        n=Counter(nums)

        result=[0,0]
        for i in n:
            if n[i]==2:
                result[0]+=1
            elif n[i]>2:
                result[0]+=n[i]//2
                if n[i]%2!=0:
                    result[1]+=1
            else:
                result[1]+=1
        return result