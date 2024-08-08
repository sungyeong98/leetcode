class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        n=list(map(str,nums))
        temp=''.join(n)
        num_list=temp.split('0')
        if len(num_list)==1:
            return len(num_list[0])-1

        result=[]
        for i in range(len(num_list)-1):
            length=len(num_list[i])+len(num_list[i+1])
            result.append(length)
        
        return max(result)