class Solution:
    def validPalindrome(self, s: str) -> bool:
        def find(s,left,right,deleted):
            while left<right:
                if s[left]!=s[right]:
                    if deleted:
                        return False
                    else:
                        return find(s,left+1,right,True) or find(s,left,right-1,True)
                else:
                    left+=1
                    right-=1
            return True
        return find(s,0,len(s)-1,False)