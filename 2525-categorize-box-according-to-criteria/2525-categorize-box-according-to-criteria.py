class Solution:
    def categorizeBox(self, length: int, width: int, height: int, mass: int) -> str:
        volume=length*width*height
        Bulky,Heavy=False,False

        if volume>=10**9:
            Bulky=True
        if mass>=100:
            Heavy=True
        
        if Bulky and Heavy: return 'Both'
        elif not Bulky and not Heavy:   return 'Neither'
        elif Bulky and not Heavy:   return 'Bulky'
        else:   return 'Heavy'