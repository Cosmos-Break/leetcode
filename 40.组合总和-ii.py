#
# @lc app=leetcode.cn id=40 lang=python3
#
# [40] 组合总和 II
#

# @lc code=start
from typing import List


class Solution:

    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        def dfs(begin, path, residue):
            if residue == 0:
                res.append(path[:])
                return
            for index in range(begin, size):
                if candidates[index] > residue:
                    break
                if index > begin and candidates[index - 1] == candidates[index]:
                    continue
                path.append(candidates[index])
                dfs(index + 1, path, residue - candidates[index])
                path.pop()
        size = len(candidates)
        if size == 0:
            return []
        candidates.sort()
        res = []
        dfs(0, [], target)
        return res
# @lc code=end

