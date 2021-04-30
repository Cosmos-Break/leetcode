#
# @lc app=leetcode.cn id=905 lang=python3
#
# [905] 按奇偶排序数组
#

# @lc code=start
# class Solution:
#     def sortArrayByParity(self, A: List[int]) -> List[int]:
#         return sorted(A, key=lambda x:x % 2 != 0)
class Solution(object):
    def sortArrayByParity(self, A):
        return ([x for x in A if x % 2 == 0] +
                [x for x in A if x % 2 == 1])

# @lc code=end

