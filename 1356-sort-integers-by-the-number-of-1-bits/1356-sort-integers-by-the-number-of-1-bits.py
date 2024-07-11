class Solution:
    def sortByBits(self, arr: List[int]) -> List[int]:
        temp={i:bin(i)[2:].count('1') for i in arr}
        return list(sorted(temp.keys(), key=lambda x:(temp[x],x)))