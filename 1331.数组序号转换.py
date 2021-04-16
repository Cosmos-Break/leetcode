#
# @lc app=leetcode.cn id=1331 lang=python3
#
# [1331] 数组序号转换
#

# @lc code=start
class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        sort_arr = sorted(list(set(arr)))
        arr_dict = dict()
        for k, v in enumerate(sort_arr):
            arr_dict[v] = k+1
        return [arr_dict[i] for i in arr]
  
# @lc code=end

