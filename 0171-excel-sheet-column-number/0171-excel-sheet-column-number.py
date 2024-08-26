class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        temp={chr(i):i-ord('A')+1 for i in range(ord('A'), ord('Z')+1)}
        result=0

        for idx, val in enumerate(columnTitle[::-1]):
            result+=temp[val]*26**idx
        return result