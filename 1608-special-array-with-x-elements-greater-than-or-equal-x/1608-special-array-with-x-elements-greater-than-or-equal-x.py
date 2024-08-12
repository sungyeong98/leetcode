class Solution:
    def specialArray(self, nums: List[int]) -> int:
        counter=Counter(nums)
        counter=dict(sorted(counter.items(), key=lambda x:x[0]))

        total_cnt=sum([i for i in counter.values()])
        for num in range(max(nums)+1):
            if num==total_cnt:
                return num
            
            if num in counter:
                total_cnt-=counter[num]
        return -1