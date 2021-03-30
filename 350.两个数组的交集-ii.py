# @before-stub-for-debug-begin
from python3problem350 import *
from typing import *
# @before-stub-for-debug-end

#
# @lc app=leetcode.cn id=350 lang=python3
#
# [350] 两个数组的交集 II
#
import collections
# @lc code=start
class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        num1 = collections.Counter(nums1)
        num2 = collections.Counter(nums2)
        num = num1 & num2
        return list(num.elements())
# @lc code=end

