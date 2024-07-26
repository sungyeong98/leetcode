class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        result=0
        c=set(chars)
        cc=Counter(chars)
        for word in words:
            n=len(word)
            if len(set(word)&c)==len(set(word)):
                counter=Counter(word)
                flag=True
                for w in counter:
                    if counter[w]>cc[w]:
                        flag=False
                        break
                if flag:
                    result+=n
        return result