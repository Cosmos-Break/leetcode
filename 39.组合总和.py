#
# @lc app=leetcode.cn id=39 lang=python3
#
# [39] 组合总和
#
# from typing import List
# @lc code=start
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        result_list = []
        result = []
        def generate(candidates, target, result):
            if target < 0:
                return
            if target == 0:
                result_list.append(result)
                return
            for i in range(len(candidates)):
                generate(candidates[i:], target - candidates[i], result+[candidates[i]])
        generate(candidates, target, result)
        return result_list
# @lc code=end
# s = Solution()
# s.combinationSum([2,3,6,7], 7)
