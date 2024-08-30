class Solution:
    def haveConflict(self, event1: List[str], event2: List[str]) -> bool:
        e1=[int(i.split(':')[0])*60+int(i.split(':')[1]) for i in event1]
        e2=[int(i.split(':')[0])*60+int(i.split(':')[1]) for i in event2]
        for i in e1:
            if e2[0]<=i<=e2[1]:
                return True
        for i in e2:
            if e1[0]<=i<=e1[1]:
                return True
        return False