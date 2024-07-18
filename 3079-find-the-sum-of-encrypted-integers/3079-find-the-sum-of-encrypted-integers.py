class Solution:
    def sumOfEncryptedInt(self, nums: List[int]) -> int:
        result=0
        for num in nums:
            temp=list(map(int,str(num)))
            max_num=max(temp)
            n=len(temp)
            result+=int(str(max_num)*n)
        return result