class Solution:
    def makeEqual(self, words: List[str]) -> bool:
        n=len(words)
        if n<=1:    return True
        counter=Counter()
        for word in words:
            counter.update(Counter(word))
        for i in counter:
            num=counter[i]
            if num%n!=0:
                return False
        return True