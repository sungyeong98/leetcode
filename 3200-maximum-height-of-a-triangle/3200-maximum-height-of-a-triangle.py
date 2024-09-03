class Solution:
    def maxHeightOfTriangle(self, red: int, blue: int) -> int:
        def count(a,b):
            height, idx = 0, 1
            while True:
                if idx%2==1:
                    if a>=idx:
                        a-=idx
                    else:
                        break
                else:
                    if b>=idx:
                        b-=idx
                    else:
                        break
                height+=1
                idx+=1
            return height
        return max(count(red,blue),count(blue,red))