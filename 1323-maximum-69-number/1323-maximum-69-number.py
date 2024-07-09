class Solution:
    def maximum69Number (self, num: int) -> int:
        n=list(str(num))
        for i in range(len(n)):
            if n[i]=='6':
                n[i]='9'
                return int(''.join(n))
        return num