class Solution:
    def checkTwoChessboards(self, coordinate1: str, coordinate2: str) -> bool:
        c1,v1=coordinate1[0],coordinate1[1]
        c2,v2=coordinate2[0],coordinate2[1]
        if (c1 in 'aceg' and c2 in 'aceg') or (c1 in 'befh' and c2 in 'befh'):
            if int(v1)%2==int(v2)%2:
                return True
            else:
                return False
        else:
            if int(v1)%2!=int(v2)%2:
                return True
            else:
                return False