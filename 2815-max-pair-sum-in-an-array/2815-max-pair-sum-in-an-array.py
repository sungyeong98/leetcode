class Solution:
    def maxSum(self, nums: List[int]) -> int:
        large_num=defaultdict(list)
        for i in nums:
            temp=int(sorted(str(i))[-1])
            large_num[temp].append(i)
        result=0
        target_key=[i for i in large_num.keys() if len(large_num[i])>=2]
        if not target_key:
            return -1
        for key in target_key:
            temp=sorted(large_num[key])
            result=max(result,temp[-1]+temp[-2])
        return result