class Solution:
    def buildArray(self, target: List[int], n: int) -> List[str]:
        result=[]
        cnt,idx=1,0
        while cnt<=n:
            if target[idx]==cnt:
                result.append('Push')
                cnt+=1
                idx+=1
                if cnt>target[-1]:
                    break
            else:
                result.append('Push')
                result.append('Pop')
                cnt+=1
        return result
        