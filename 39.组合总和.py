#
# @lc app=leetcode.cn id=39 lang=python3
#
# [39] 组合总和
#
# from typing import List
# @lc code=start
from typing import List


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        def dfs(candidates, begin, size, path, res, target):
            if target < 0:
                return
            if target == 0:
                res.append(path)
                return

            for index in range(begin, size):
                if target - candidates[index] < 0:
                    break
                dfs(candidates, index, size, path + [candidates[index]], res, target - candidates[index])
        size = len(candidates)
        if size == 0:
            return []
        path = []
        res = []
        candidates.sort()
        dfs(candidates, 0, size, path, res, target)
        return res

# @lc code=end
# s = Solution()
# s.combinationSum([2,3,6,7], 7)
