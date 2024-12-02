class Solution:
    def isBalanced(self, num: str) -> bool:
        even = sum([int(val) for idx, val in enumerate(num) if idx%2==0])
        odd = sum([int(val) for idx, val in enumerate(num) if idx%2==1])

        return even==odd