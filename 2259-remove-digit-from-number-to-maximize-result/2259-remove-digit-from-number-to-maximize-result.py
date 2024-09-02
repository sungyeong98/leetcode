class Solution:
    def removeDigit(self, number: str, digit: str) -> str:
        idx=[idx for idx,val in enumerate(number) if val==digit]
        result=0
        for i in idx:
            temp=number[:i]+number[i+1:]
            result=max(result,int(temp))
        return str(result)