from collections import defaultdict
class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        temp=defaultdict(chr)
        for i in range(len(s)):
            temp[i]=s[indices.index(i)]
        result=''
        for i in temp:
            result+=temp[i]
        return result