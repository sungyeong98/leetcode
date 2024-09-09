class Solution:
    def largestOverlap(self, img1: List[List[int]], img2: List[List[int]]) -> int:
        a,b,d=[],[],defaultdict(int)
        for r in range(len(img1)):
            for c in range(len(img1[0])):
                if img1[r][c]:
                    a.append((r,c))
                if img2[r][c]:
                    b.append((r,c))
        for ra,ca in a:
            for rb,cb in b:
                d[(rb-ra,cb-ca)]+=1
        return max(d.values() or [0])