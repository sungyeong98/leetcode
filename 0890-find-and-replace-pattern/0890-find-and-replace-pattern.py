class Solution:
    def findAndReplacePattern(self, words: List[str], pattern: str) -> List[str]:
        if len(pattern)==1: return words

        result=[]
        for i in words:
            temp1,temp2={},{}
            flag=True
            for w1,w2 in zip(i,pattern):
                if w1 in temp1:
                    if temp1[w1]!=w2:
                        flag=False
                        break
                else:
                    temp1[w1]=w2
                
                if w2 in temp2:
                    if temp2[w2]!=w1:
                        flag=False
                        break
                else:
                    temp2[w2]=w1
            
            if flag:
                result.append(i)
        return result