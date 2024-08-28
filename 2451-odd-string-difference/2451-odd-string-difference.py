class Solution:
    def oddString(self, words: List[str]) -> str:
        result=defaultdict(list)
        for word in words:
            n=len(word)
            temp=[]
            for idx in range(n-1):
                left=ord(word[idx])-ord('a')
                right=ord(word[idx+1])-ord('a')
                temp.append(right-left)
            result[tuple(temp)].append(word)
        return min(result.values(), key=len)[0]