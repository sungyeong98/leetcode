class Solution:
    def diffWaysToCompute(self, expression: str) -> List[int]:
        def backtrack(exp):
            if exp.isdigit():
                return [int(exp)]
            result=[]

            for idx, char in enumerate(exp):
                if char in '+-*':
                    left=backtrack(exp[:idx])
                    right=backtrack(exp[idx+1:])

                    for l in left:
                        for r in right:
                            if char=='+':
                                result.append(l+r)
                            elif char=='-':
                                result.append(l-r)
                            else:
                                result.append(l*r)
            return result
        result=backtrack(expression)
        return sorted(result)