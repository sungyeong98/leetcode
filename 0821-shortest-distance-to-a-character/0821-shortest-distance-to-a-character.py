class Solution:
    def shortestToChar(self, s: str, c: str) -> List[int]:
        target=[idx for idx,val in enumerate(s) if val==c]

        result=[]
        for idx,val in enumerate(s):
            if val==c:
                result.append(0)
            else:
                temp=int(1e9)
                for t in target:
                    if abs(t-idx)<temp:
                        temp=abs(t-idx)
                    else:
                        break
                result.append(temp)
        return result