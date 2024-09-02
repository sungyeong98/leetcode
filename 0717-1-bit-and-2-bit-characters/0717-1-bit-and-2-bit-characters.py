class Solution:
    def isOneBitCharacter(self, bits: List[int]) -> bool:
        if len(bits)<=2:
            return True
        return True if len(bits)%2==1 else False