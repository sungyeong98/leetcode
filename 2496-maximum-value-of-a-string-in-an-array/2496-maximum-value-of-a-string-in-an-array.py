class Solution:
    def maximumValue(self, strs: List[str]) -> int:
        temp=[int(i) if i.isdigit() else len(i) for i in strs]
        return max(temp)