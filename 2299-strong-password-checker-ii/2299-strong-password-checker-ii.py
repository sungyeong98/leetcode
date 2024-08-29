class Solution:
    def strongPasswordCheckerII(self, password: str) -> bool:
        n=len(password)
        if n<8: return False
        l,h,d,s=False,False,False,False
        for i in range(n-1):
            left,right=password[i],password[i+1]
            if not l and (left.islower() or right.islower()):
                l=True
            if not h and (left.isupper() or right.isupper()):
                h=True
            if not d and (left.isdigit() or right.isdigit()):
                d=True
            if not s and (left in "!@#$%^&*()-+" or right in "!@#$%^&*()-+"):
                s=True
            
            if left==right:
                return False
        
        return l&h&d&s