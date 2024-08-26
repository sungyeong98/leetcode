class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        def count(s,left,right):
            if right-left==1:
                return 1
            
            cnt=0
            for i in range(left,right):
                if s[i]=='(':
                    cnt+=1
                if s[i]==')':
                    cnt-=1
                if cnt==0:
                    return count(s,left,i)+count(s,i+1,right)
            return 2*count(s,left+1, right-1)
        return count(s,0,len(s)-1)