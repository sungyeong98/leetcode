class Solution:
    def convertDateToBinary(self, date: str) -> str:
        temp=[]
        for i in date.split('-'):
            temp.append(bin(int(i))[2:])
        return '-'.join(temp)