class Solution:
    def findLexSmallestString(self, s: str, a: int, b: int) -> str:
        def add(s,a):
            s=list(s)
            n=len(s)
            for i in range(1,n,2):
                s[i]=str((int(s[i])+a)%10)
            return ''.join(s)
        def rotate(s,b):
            return s[-b:]+s[:-b]

        visited=set()
        q=deque([s])
        min_s=s

        while q:
            cur=q.popleft()

            if cur<min_s:
                min_s=cur
            
            new_s=add(cur,a)
            if new_s not in visited:
                visited.add(new_s)
                q.append(new_s)
            
            new_s=rotate(cur,b)
            if new_s not in visited:
                visited.add(new_s)
                q.append(new_s)
        return min_s