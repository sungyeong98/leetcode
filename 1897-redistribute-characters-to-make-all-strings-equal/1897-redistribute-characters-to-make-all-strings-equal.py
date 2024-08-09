class Solution:
    def makeEqual(self, words: List[str]) -> bool:
        n=len(words)
        if n<=1:    return True
        counter=Counter()
        for word in words:
            counter.update(Counter(word))
        result=[i for i in counter.values() if ((i>=n and i%n==0) or (i<n and i%2==n%2))]
        return len(result)==n