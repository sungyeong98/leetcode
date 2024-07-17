class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        result=0
        for i in list(zip(*strs)):
            temp1=list(i)
            temp2=list(i)
            temp2.sort()
            if temp1!=temp2:
                result+=1
        return result