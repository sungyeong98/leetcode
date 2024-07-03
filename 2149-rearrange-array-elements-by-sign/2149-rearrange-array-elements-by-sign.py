class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        pos,neg=[i for i in nums if i>0],[i for i in nums if i<0]
        temp=[]
        for i,j in zip(pos,neg):
            temp.append(i)
            temp.append(j)
        return temp