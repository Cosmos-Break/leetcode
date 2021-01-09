#
# @lc app=leetcode.cn id=33 lang=python3
#
# [33] 搜索旋转排序数组
#

# @lc code=start
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        try:
            index = nums.index(target)
        except:
            index = -1
        return index
# @lc code=end

