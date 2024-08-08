class Solution:
    def findLucky(self, arr: List[int]) -> int:
        counter=Counter(arr)
        result=[]
        for num in counter:
            if num==counter[num]:
                result.append(num)
        return max(result) if result else -1