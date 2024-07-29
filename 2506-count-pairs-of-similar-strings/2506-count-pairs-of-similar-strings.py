class Solution:
    def similarPairs(self, words: List[str]) -> int:
        result=0
        w=deque([set(i) for i in words])
        while w:
            c=w.popleft()
            for i in w:
                if c==i:
                    result+=1
        return result