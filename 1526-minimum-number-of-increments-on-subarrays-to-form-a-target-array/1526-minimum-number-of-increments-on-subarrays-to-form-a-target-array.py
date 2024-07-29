class Solution:
    def minNumberOperations(self, target: List[int]) -> int:
        prev=0
        result=0

        for val in target:
            result+=val-prev if val>prev else 0
            prev=val
        return result