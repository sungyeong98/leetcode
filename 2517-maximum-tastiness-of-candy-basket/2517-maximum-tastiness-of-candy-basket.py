class Solution:
    def maximumTastiness(self, price: List[int], k: int) -> int:
        price.sort()

        def search(x):
            prev, cnt, i = price[0], 1, 1
            while cnt<k and i<len(price):
                if price[i]-prev>=x:
                    prev, cnt = price[i], cnt+1
                i+=1
            return cnt==k

        left,right=0,10**9
        while left<right:
            mid=(left+right)//2
            if search(mid):
                left=mid+1
            else:
                right=mid
        
        return left-1