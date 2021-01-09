#
# @lc app=leetcode.cn id=167 lang=python3
#
# [167] 两数之和 II - 输入有序数组
#
# from typing import List
# @lc code=start
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        for i in range(len(numbers)):
            a = target - numbers[i]
            if a in numbers[i+1:]:
                return [i + 1, numbers.index(a,i+1) + 1]
        return None

# @lc code=end

# s = Solution()
# s.twoSum([2,7,11,15], 9)
