class Solution:
    def circularGameLosers(self, n: int, k: int) -> List[int]:
        cnt=[0]*n
        pos,i=0,1
        cnt[pos]+=1
        while True:
            pos=(pos+i*k)%n
            cnt[pos]+=1
            if cnt[pos]>1:
                break
            i+=1
        return [idx+1 for idx,val in enumerate(cnt) if val==0]