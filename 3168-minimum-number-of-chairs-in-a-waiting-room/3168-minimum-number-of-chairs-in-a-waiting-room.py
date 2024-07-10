class Solution:
    def minimumChairs(self, s: str) -> int:
        result=[0]
        for i in list(s):
            if i=='E':
                result.append(result[-1]+1)
            else:
                result.append(result[-1]-1)
        return max(result)
        