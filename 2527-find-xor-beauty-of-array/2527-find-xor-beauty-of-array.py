class Solution:
    def xorBeauty(self, nums: List[int]) -> int:
        n=len(nums)
        result=0

        for bit in range(32):
            bit_mask=1<<bit
            count=0

            for i in range(n):
                for j in range(n):
                    if (nums[i]|nums[j])&bit_mask:
                        count+=1
            
            cnt=0
            for k in range(n):
                if nums[k]&bit_mask:
                    cnt+=1
            
            total_cnt=count*cnt
            if total_cnt%2==1:
                result|=bit_mask
        return result