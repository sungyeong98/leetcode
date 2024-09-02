class Solution:
    def canBeEqual(self, s1: str, s2: str) -> bool:
        for i in range(2):
            left,right=i,i+2
            if s1[left]==s2[left] and s1[right]==s2[right]:
                continue
            elif s1[left]==s2[right] and s1[right]==s2[left]:
                continue
            else:
                return False
        return True