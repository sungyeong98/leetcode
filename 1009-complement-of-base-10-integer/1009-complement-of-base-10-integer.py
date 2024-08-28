class Solution:
    def bitwiseComplement(self, n: int) -> int:
        temp=''
        for i in bin(n)[2:]:
            if i=='0':
                temp+='1'
            else:
                temp+='0'
        return int(temp,2)