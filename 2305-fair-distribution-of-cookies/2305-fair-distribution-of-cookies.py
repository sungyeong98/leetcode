class Solution:
    def distributeCookies(self, cookies: List[int], k: int) -> int:
        result=int(1e9)
        def backtrack(children,c,cur_max):
            nonlocal result
            if not c:
                result=min(result,cur_max)
                return
            num=c.pop()
            for i in range(k):
                children[i]+=num
                next_max=max(cur_max, children[i])
                if next_max<result:
                    backtrack(children,c,next_max)
                children[i]-=num
            c.append(num)

        backtrack([0]*k,cookies,0)
        return result