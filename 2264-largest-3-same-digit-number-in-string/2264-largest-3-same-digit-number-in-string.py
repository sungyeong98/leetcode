class Solution:
    def largestGoodInteger(self, num: str) -> str:
        result=[]
        for i in range(len(num)-2):
            if len(set(num[i:i+3]))==1:
                result.append(num[i:i+3])
        if result:
            return max(result)
        return ''