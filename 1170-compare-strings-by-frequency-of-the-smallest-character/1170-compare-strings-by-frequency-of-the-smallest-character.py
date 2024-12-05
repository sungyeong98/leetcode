class Solution:
    def numSmallerByFrequency(self, queries: List[str], words: List[str]) -> List[int]:
        def helper(s):
            temp = sorted(list(s))[0]
            return s.count(temp)
        
        q, w = [helper(i) for i in queries], [helper(i) for i in words]
        result = []

        for i in q:
            cnt = 0
            for j in w:
                if i<j:
                    cnt+=1
            result.append(cnt)
        
        return result