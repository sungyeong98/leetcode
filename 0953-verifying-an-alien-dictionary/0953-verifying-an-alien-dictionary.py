class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        wd={chr(i+97):order[i] for i in range(len(order))}
        temp=[]
        for idx,word in enumerate(words):
            w=''.join(wd[i] for i in word)
            temp.append((w,idx))
        result=[i[1] for i in sorted(temp)]
        return True if result==list(range(len(result))) else False