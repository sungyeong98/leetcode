class Solution:
    def partition(self, s: str) -> List[List[str]]:
        def isvalid(sub):
            return sub==sub[::-1]
        def backtrack(start,path):
            if start==len(s):
                result.append(path[:])
                return
            for end in range(start+1, len(s)+1):
                substring=s[start:end]
                if isvalid(substring):
                    path.append(substring)
                    backtrack(end,path)
                    path.pop()

        result=[]
        backtrack(0,[])
        return result