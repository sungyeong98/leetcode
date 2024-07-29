class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        if sum([i for i in range(1,k+1)])>n:    return []

        result=[]

        def backtrack(comb):
            if len(comb)>k or sum(comb)>n:
                return
            
            if len(comb)==k and sum(comb)==n:
                result.append(comb)
                return
            
            for i in range(1,10):
                if i not in comb and comb[-1]<i:
                    backtrack(comb+[i])
            
            return comb
        for i in range(1,10):
            backtrack([i])
        return result