class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        left=[idx for idx,val in enumerate(s) if val=='(']
        right=[idx for idx,val in enumerate(s) if val==')']
        l=r=0
        while left and right and r<len(right):
            if left[l]<right[r]:
                left.pop(l)
                right.pop(r)
            else:
                r+=1

        result=''
        for idx,val in enumerate(s):
            if idx in left or idx in right:
                continue
            else:
                result+=val

        return result