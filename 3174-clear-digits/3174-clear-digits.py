class Solution:
    def clearDigits(self, s: str) -> str:
        result=[]
        for i in s:
            if i.isalpha():
                result.append(i)
            else:
                result.pop()
        return ''.join(result)