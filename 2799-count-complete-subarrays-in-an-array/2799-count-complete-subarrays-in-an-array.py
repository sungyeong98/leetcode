class Solution:
    def countCompleteSubarrays(self, nums: List[int]) -> int:
        n=len(nums)
        dis_num=len(set(nums))
        cnt, left, right = 0, 0, 0
        counter=Counter()
        
        while right<n:
            counter[nums[right]]+=1
            while len(counter)==dis_num:
                counter[nums[left]]-=1
                if counter[nums[left]]==0:
                    del counter[nums[left]]
                left+=1
                cnt+=(n-right)
            right+=1
        return cnt