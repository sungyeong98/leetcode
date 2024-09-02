class Solution:
    def addToArrayForm(self, num: List[int], k: int) -> List[int]:
        n=len(num)
        for i in range(n-1,-1,-1):
            k,num[i]=divmod(num[i]+k,10)
        while k:
            k,a=divmod(k,10)
            num=[a]+num
        return num