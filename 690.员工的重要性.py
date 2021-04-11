#
# @lc app=leetcode.cn id=690 lang=python3
#
# [690] 员工的重要性
#

# @lc code=start
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
        edict = {e.id:e for e in employees}
        def dfs(id):
            return edict[id].importance + sum(dfs(id_down) for id_down in edict[id].subordinates)
        return dfs(id)
# @lc code=end

