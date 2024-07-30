class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        #solution1
        '''
        avg=sum(weights)//days
        result=0

        while True:
            if max(weights)>avg:
                avg+=1
                continue

            total=1
            sub=0
            for i in weights:
                if sub+i<=avg:
                    sub+=i
                else:
                    total+=1
                    sub=i

            if total>days:
                avg+=1
            else:
                result=avg
                return result
        '''
        def isValid(cap):
            day,total=1,0
            for w in weights:
                total+=w
                if total>cap:
                    total=w
                    day+=1
                    if day>days:
                        return False
            return True

        left,right=max(weights),sum(weights)
        while left<right:
            mid=(left+right)//2

            if isValid(mid):
                right=mid
            else:
                left=mid+1
        return left