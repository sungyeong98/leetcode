class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        small,same,big=[],[],[]
        for i in nums:
            if i<pivot:
                small.append(i)
            elif i==pivot:
                same.append(i)
            else:
                big.append(i)
        return small+same+big