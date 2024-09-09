class Solution:
    def distMoney(self, money: int, children: int) -> int:
        if money<children:
            return -1
        n=8*children - money
        if n<=0:
            return children-(n<0)
        result,rem=divmod(money-children, 7)
        return result-((result,rem)==(children-1,3))