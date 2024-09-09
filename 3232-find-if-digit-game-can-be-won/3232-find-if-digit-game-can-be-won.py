class Solution:
    def canAliceWin(self, nums: List[int]) -> bool:
        temp=sum(filter(lambda x:x<10,nums))
        sum_num=sum(nums)
        return sum_num%2!=0 or temp!=sum_num//2