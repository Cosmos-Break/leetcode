#
# @lc app=leetcode.cn id=40 lang=python3
#
# [40] 组合总和 II
#

# @lc code=start
class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        result_list = []
        result = []
        def generate(candidates, target, result):
            if target < 0:
                return
            if target == 0:
                result_list.append(result)
                return
            for i in range(len(candidates)):
                generate(candidates[i + 1:], target - candidates[i], result+[candidates[i]])
        generate(candidates, target, result)
        return result_list
# @lc code=end

