class Solution:
    def largestCombination(self, candidates: List[int]) -> int:
        temp=defaultdict(int)
        for num in candidates:
            bits=bin(num)[2:][::-1]
            for idx,val in enumerate(bits):
                if val=='1':
                    temp[idx]+=1
        return max(temp.values())