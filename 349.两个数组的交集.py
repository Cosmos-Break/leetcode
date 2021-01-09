#
# @lc app=leetcode.cn id=349 lang=python3
#
# [349] 两个数组的交集
#

# @lc code=start
class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        res = set()
        for num1 in nums1:
            if num1 in nums2:
                res.add(num1)
        return list(res)
# @lc code=end

