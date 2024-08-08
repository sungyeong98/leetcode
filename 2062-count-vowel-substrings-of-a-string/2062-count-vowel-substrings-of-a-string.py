class Solution:
    def countVowelSubstrings(self, word: str) -> int:
        result=0
        temp=defaultdict(int)

        for idx, w in enumerate(word):
            if w in 'aeiou':
                if not idx or word[idx-1] not in 'aeiou':
                    jj=j=idx
                    temp.clear()
                temp[w]+=1
                while len(temp)==5 and all(temp.values()):
                    temp[word[j]]-=1
                    j+=1
                result+=j-jj
        return result