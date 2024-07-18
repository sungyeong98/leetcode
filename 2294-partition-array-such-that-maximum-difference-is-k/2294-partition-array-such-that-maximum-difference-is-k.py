class Solution:
    def partitionArray(self, nums: List[int], k: int) -> int:
        nums=deque(sorted(nums))
        result, min_num = 0, -1
        while nums:
            if min_num<0:
                result+=1
                min_num=nums.popleft()
            else:
                num=nums.popleft()
                if num-min_num<=k:
                    continue
                else:
                    result+=1
                    min_num=num
        return result