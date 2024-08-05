class Solution:
    def numberOfLines(self, widths: List[int], s: str) -> List[int]:
        line,width=1,0
        for i in s:
            w=widths[ord(i)-ord('a')]
            if width+w<=100:
                width+=w
            else:
                line+=1
                width=w
        return [line,width]