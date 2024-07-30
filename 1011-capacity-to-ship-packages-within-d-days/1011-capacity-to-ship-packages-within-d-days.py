class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
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