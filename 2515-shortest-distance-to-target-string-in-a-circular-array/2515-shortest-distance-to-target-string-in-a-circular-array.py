class Solution:
    def closetTarget(self, words: List[str], target: str, startIndex: int) -> int:
        if target not in words: return -1
        n=len(words)
        left,right=words[startIndex],words[startIndex]
        cnt=0
        while left!=target and right!=target:
            left=words[(words.index(left)-1+n)%n]
            right=words[(words.index(right)+1)%n]
            cnt+=1
        return cnt