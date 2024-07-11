class Solution:
    def squareIsWhite(self, coordinates: str) -> bool:
        char, num = ord(coordinates[0]), int(coordinates[1])
        if char%2==1 and num%2==0:
            return True
        elif char%2==0 and num%2==1:
            return True
        return False