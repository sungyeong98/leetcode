"""
# Definition for Employee.
class Employee:
    def __init__(self, id: int, importance: int, subordinates: List[int]):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates
"""

class Solution:
    def getImportance(self, employees: List['Employee'], id: int) -> int:
        def dfs(emp):
            imp=emps[emp].importance
            for i in emps[emp].subordinates:
                imp+=dfs(i)
            return imp
        emps={emp.id:emp for emp in employees}
        return dfs(id)