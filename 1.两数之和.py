#
# @lc app=leetcode.cn id=1 lang=python3
#
# [1] 两数之和
#

# @lc code=start

from typing import List
# class Solution:
#     def twoSum(self, nums: List[int], target: int) -> List[int]:
#         n = len(nums)
#         for i in range(n):
#             for j in range(i + 1, n):
#                 if nums[i] + nums[j] == target:
#                     return [i, j]

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashtable = {}
        n = len(nums)
        for i in range(n):
            if target - nums[i] not in hashtable:
                hashtable[nums[i]] = i
            else:
                return [hashtable[target-nums[i]], i]

# @lc code=end
# 第一个是暴力法， 第二个是哈希表法，当时没有想到哈希表里面存的是什么，还有应该判断什么条件
# 哈希表里面存的是数组中的一个元素和对应的索引，分别作为key和value。
# 遍历给定数组, 如果target-nums[i]不在哈希表里,则把遍历到的数nums[i]加入哈希表
# 如果target-nums[i]在哈希表里面, 那么说明这个数已经被遍历过了, 那么只要返回他的索引和当前索引


s = Solution()
print(s.twoSum([2, 7, 11, 15], 9))

