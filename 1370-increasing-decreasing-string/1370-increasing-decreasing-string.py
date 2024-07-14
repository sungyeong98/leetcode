from collections import Counter
class Solution:
    def sortString(self, s: str) -> str:
        n=len(s)
        counter=Counter(s)
        s=list(set(s))

        forward_list=sorted(s)
        backward_list=sorted(s,reverse=True)

        result,flag='',True
        while len(result)<n:
            if flag:
                for s in forward_list:
                    if counter[s]>0:
                        result+=s
                        counter[s]-=1
                flag=False
            else:
                for s in backward_list:
                    if counter[s]>0:
                        result+=s
                        counter[s]-=1
                flag=True
        return result