class Solution:
    def checkDistances(self, s: str, distance: List[int]) -> bool:
        temp={}
        for idx, val in enumerate(s):
            if val not in temp:
                temp[val]=idx
            else:
                dis=distance[ord(val)-ord('a')]
                if dis!=idx-temp[val]-1:
                    return False
        return True