class Solution:
    def findKthBit(self, n: int, k: int) -> str:
        s = '0'
        cnt = 1
        while cnt<n:
            rev_s=''
            for i in reversed(s):
                if i=='0':
                    rev_s+='1'
                else:
                    rev_s+='0'

            temp = s + '1' + rev_s
            cnt+=1
            s = temp
        print(s)
        return s[k-1]