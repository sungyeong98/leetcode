class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        result=[]
        for i in range(len(prices)):
            p=prices[i]
            if i<len(prices)-1:
                for j in range(i+1,len(prices)):
                    if p>=prices[j]:
                        p-=prices[j]
                        break
            result.append(p)
        return result