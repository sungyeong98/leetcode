class Solution:
    def totalMoney(self, n: int) -> int:
        week,day=n//7, n%7
        result=0
        if week>0:
            result+=(28*week)+sum([7*i for i in range(week-1,-1,-1)])
        m=0
        if day>0:
            m+=reduce(lambda x,y:x+y, list(range(week+1,week+day+1)))

        return result+m