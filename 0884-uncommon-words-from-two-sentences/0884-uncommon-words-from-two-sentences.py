class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        result=[]
        temp=s1.split(' ')+s2.split(' ')
        counter=Counter(temp)
        for i in counter:
            if counter[i]==1:
                result.append(i)
        return result