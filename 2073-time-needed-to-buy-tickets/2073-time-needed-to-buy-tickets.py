class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        people={i:[tickets[i],0] for i in range(len(tickets))}
        time=1
        while people[k][0]>0:
            
            for p in people:
                if people[p][0]>0:
                    people[p][0]-=1
                    people[p][1]=time
                    time+=1
        return people[k][1]