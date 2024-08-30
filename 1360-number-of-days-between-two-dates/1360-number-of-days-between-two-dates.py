from datetime import datetime
class Solution:
    def daysBetweenDates(self, date1: str, date2: str) -> int:
        d1=datetime.strptime(''.join(date1.split('-')),'%Y%m%d')
        d2=datetime.strptime(''.join(date2.split('-')),'%Y%m%d')
        temp=d2-d1
        return abs(temp.days)