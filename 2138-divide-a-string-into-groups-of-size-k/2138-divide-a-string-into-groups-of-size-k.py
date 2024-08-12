class Solution:
    def divideString(self, s: str, k: int, fill: str) -> List[str]:
        result=[]

        while s:
            temp=s[:k]
            if len(temp)==k:
                result.append(temp)
            else:
                while len(temp)<k:
                    temp+=fill
                result.append(temp)
            s=s[k:]
        
        return result