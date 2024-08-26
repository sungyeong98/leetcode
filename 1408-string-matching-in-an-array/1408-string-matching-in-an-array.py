class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        result=[]
        for target in words:
            flag=False
            for word in words:
                if target!=word and target in word:
                    flag=True
                    break
            if flag:
                result.append(target)
        return result