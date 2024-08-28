class Solution:
    def averageValue(self, nums: List[int]) -> int:
        temp=[]
        for i in nums:
            if i%2==0 and i%3==0:
                temp.append(i)
        return sum(temp)//len(temp) if temp else 0