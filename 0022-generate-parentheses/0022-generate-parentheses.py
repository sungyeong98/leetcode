class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        if n==0:
            return ['']
        result=[]
        for i in range(n):
            for left in self.generateParenthesis(i):
                for right in self.generateParenthesis(n-1-i):
                    result.append(f'({left}){right}')
        return result