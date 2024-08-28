class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        target={'b','a','l','o','n'}
        t=Counter(text)
        result=[]
        for i in target:
            if i=='l' or i=='o':
                result.append(t[i]//2)
            else:
                result.append(t[i])
        return min(result)
