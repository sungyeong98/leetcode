class Solution:
    def accountBalanceAfterPurchase(self, purchaseAmount: int) -> int:
        p=((purchaseAmount-5)//10)*10+10
        result=100-p
        return result