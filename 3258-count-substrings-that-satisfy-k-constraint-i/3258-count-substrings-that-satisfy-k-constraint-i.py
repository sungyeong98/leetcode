class Solution:
    def countKConstraintSubstrings(self, s: str, k: int) -> int:
        result, l, ones = 0, 0, 0
        for idx, word in enumerate(s):
            ones+=1 if word=='1' else 0
            while ones>k and idx-l+1-ones>k:
                ones-=1 if s[l]=='1' else 0
                l+=1
            result+=idx-l+1
        return result