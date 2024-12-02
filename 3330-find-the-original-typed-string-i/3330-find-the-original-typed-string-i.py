class Solution:
    def possibleStringCount(self, word: str) -> int:
        n, cnt = len(word), 1
        for i in range(n):
            if i+1<n and word[i]==word[i+1]:
                cnt+=1
        return cnt