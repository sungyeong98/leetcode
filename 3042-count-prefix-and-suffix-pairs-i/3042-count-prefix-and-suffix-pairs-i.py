class Solution:
    def countPrefixSuffixPairs(self, words: List[str]) -> int:
        n, result = len(words), 0

        def isvalid(str1,str2):
            if len(str1)>len(str2):
                return False
            
            if str1!=str2[:len(str1)] or str1!=str2[-len(str1):]:
                return False
            return True

        for i in range(n-1):
            prefix=words[i]
            for j in range(i+1,n):
                suffix=words[j]
                if isvalid(prefix, suffix):
                    result+=1
        return result