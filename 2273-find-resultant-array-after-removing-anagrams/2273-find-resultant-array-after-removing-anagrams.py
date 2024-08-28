class Solution:
    def removeAnagrams(self, words: List[str]) -> List[str]:
        idx=0
        while words:
            if idx>=len(words)-1:
                break
            left=sorted(words[idx])
            right=sorted(words[idx+1])
            if len(left)!=len(right) or left!=right:
                idx+=1
            else:
                words.pop(idx+1)
        return words