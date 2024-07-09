class Solution:
    def averageWaitingTime(self, customers: List[List[int]]) -> float:
        n=len(customers)
        total_time, cur_time, wait_time = 0, 0, 0
        for arrival_time, load_time in customers:
            if cur_time<arrival_time:
                cur_time=arrival_time
                total_time+=load_time
                cur_time+=load_time
            else:
                wait_time=cur_time-arrival_time
                total_time+=load_time+wait_time
                cur_time+=load_time
                wait_time=0
        return total_time/n