class Solution:
    def sortJumbled(self, mapping: List[int], nums: List[int]) -> List[int]:
        mapping_num=[]
        for idx,num in enumerate(nums):
            temp=''
            for n in str(num):
                temp+=str(mapping[int(n)])
            mapping_num.append((int(temp),idx))

        mapping_idx=sorted(mapping_num,key=lambda x:(x[0],x[1]))

        return [nums[i] for _,i in mapping_idx]