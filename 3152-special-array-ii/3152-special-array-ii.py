class Solution:
    def isArraySpecial(self, nums: List[int], queries: List[List[int]]) -> List[bool]:
        temp = ['even' if i%2==0 else 'odd' for i in nums]
        result = []

        for start, end in queries:
            sublist = temp[start:end+1]
            if len(sublist)==1:
                result.append(True)
                continue
            start, end = sublist[0], sublist[1]
            t1 = set([i for i in range(len(sublist)) if i%2==0])
            t2 = set([i for i in range(len(sublist)) if i%2==1])

            if start in t2 or end in t1 or len(t1)!=1 or len(t2)!=1:
                result.append(False)
            else:
                result.append(True)
        return result