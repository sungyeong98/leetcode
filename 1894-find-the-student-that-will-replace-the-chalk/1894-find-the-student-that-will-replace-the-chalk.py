class Solution:
    def chalkReplacer(self, chalk: List[int], k: int) -> int:
        n=len(chalk)
        k=k%sum(chalk)
        idx=0
        while k>0:
            if chalk[idx]>k:
                return idx
            
            k-=chalk[idx]
            idx=(idx+1)%n
        return idx