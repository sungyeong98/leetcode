class Solution:
    def shortestCompletingWord(self, licensePlate: str, words: List[str]) -> str:
        w=defaultdict(int)
        for i in licensePlate:
            if i.isalpha():
                w[i.lower()]+=1
        
        result=[]
        for idx,word in enumerate(words):
            c=Counter(word)
            flag=True

            for j in w:
                if j not in c or w[j]!=c[j]:
                    flag=False
                    break
            
            if flag:
                result.append((word,idx))
        
        return sorted(result,key=lambda x:(len(x[0]), x[1]))[0][0]