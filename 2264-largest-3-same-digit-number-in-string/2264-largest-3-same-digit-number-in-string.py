class Solution:
    def largestGoodInteger(self, num: str) -> str:
        for i in range(len(num)-2):
            if len(set(num[i:i+3]))==1:
                return num[i:i+3]
        return ''