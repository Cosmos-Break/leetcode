#
# @lc app=leetcode.cn id=1636 lang=python3
#
# [1636] 按照频率将数组升序排序
#
from collections import Counter
# @lc code=start
class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        ret = []
        for item in Counter(nums).most_common()[::-1]:
            num = item[0]
            count = item[1]
            ret += [num] * count
        return ret
# @lc code=end

