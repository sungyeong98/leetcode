class Solution:
    def getLongestSubsequence(self, words: List[str], groups: List[int]) -> List[str]:
        one,zero=[],[]
        for idx,val in enumerate(groups):
            if not one and val==1:
                one.append((idx,val))
            if not zero and val==0:
                zero.append((idx,val))
            
            if one and one[-1][1]!=val:
                one.append((idx,val))
            if zero and zero[-1][1]!=val:
                zero.append((idx,val))
        
        if len(one)>len(zero):
            return [words[idx] for idx,_ in one]
        else:
            return [words[idx] for idx,_ in zero]