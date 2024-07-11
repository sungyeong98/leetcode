class Solution:
    def squareIsWhite(self, coordinates: str) -> bool:
        char, num = ord(coordinates[0]), int(coordinates[1])
        if (char+num)%2==1:
            return True
        return False