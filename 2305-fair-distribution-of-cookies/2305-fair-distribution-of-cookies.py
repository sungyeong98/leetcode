class Solution:
    def distributeCookies(self, cookies: List[int], k: int) -> int:
        result=[]
        def backtrack(children,c):
            if not c:
                result.append(max(children))
                return
            num=c.pop()
            for i in range(k):
                children[i]+=num
                backtrack(children,c)
                children[i]-=num
            c.append(num)
        backtrack([0]*k,cookies)
        return min(result)