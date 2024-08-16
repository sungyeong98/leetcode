class Solution:
    def maxDistance(self, colors: List[int]) -> int:
        n=len(colors)
        lleft,lright=0,n-1
        rleft,rright=0,n-1
        result=0
        while lleft<lright and rleft<rright:
            if colors[lleft]!=colors[lright]:
                result=lright-lleft
                break
            if colors[rleft]!=colors[rright]:
                result=rright-rleft
                break

            lright-=1
            rleft+=1
        return result