class Solution:
    def minFlips(self, target: str) -> int:
        start=False
        result=0
        for i in target:
            if i=='0' and start:
                result+=1
                start=False
            elif i=='1' and not start:
                result+=1
                start=True
        return result