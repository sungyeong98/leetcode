class Solution:
    def findTheLongestBalancedSubstring(self, s: str) -> int:
        result=0
        temp='01'
        while len(temp)<=len(s):
            if temp in s:
                result=len(temp)
            temp='0'+temp+'1'
        return result