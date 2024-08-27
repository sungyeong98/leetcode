class Solution:
    def average(self, salary: List[int]) -> float:
        salary.sort()
        s=salary[1:-1]
        n=len(s)
        return sum(s)/n