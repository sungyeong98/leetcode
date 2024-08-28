class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        blocks=blocks+' '
        q=deque([])
        result=float('inf')
        cnt=0
        for i in blocks:
            if len(q)==k:
                result=min(result,cnt)
                if q[0]=='W':
                    cnt-=1
                q.popleft()
            if i=='W':
                cnt+=1
            q.append(i)
        return result