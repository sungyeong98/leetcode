class Solution:
    def maximumNumberOfStringPairs(self, words: List[str]) -> int:
        n=len(words)
        result=0
        for i in range(n-1):
            for j in range(i+1, n):
                if words[i]==words[j][::-1]:
                    result+=1
        return result