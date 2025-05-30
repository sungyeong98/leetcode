class Solution:
    def maxRepeating(self, sequence: str, word: str) -> int:
        if word not in sequence:
            return 0
        
        left,right=1,len(sequence)
        while left<=right:
            mid=(left+right)//2
            if word*mid in sequence:
                left=mid+1
            else:
                right=mid-1
        return left-1