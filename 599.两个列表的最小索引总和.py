# @before-stub-for-debug-begin
from python3problem599 import *
from typing import *
# @before-stub-for-debug-end

#
# @lc app=leetcode.cn id=599 lang=python3
#
# [599] 两个列表的最小索引总和
#

# @lc code=start
class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        hash_table = {}
        for index, s in enumerate(list1):
            hash_table[s] = index
        ret = []
        min_index_sum = float("inf")
        for index, s in enumerate(list2):
            if s in hash_table:
                index_sum = hash_table[s] + index
                if min_index_sum == index_sum:
                    ret.append(s)
                elif min_index_sum > index_sum:
                    min_index_sum = index_sum
                    ret = [s]
        return ret
# @lc code=end

