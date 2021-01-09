#
# @lc app=leetcode.cn id=88 lang=python3
#
# [88] 合并两个有序数组
#
from typing import List
# @lc code=start
# class Solution:
#     def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
#         """
#         Do not return anything, modify nums1 in-place instead.
#         """
#         nums1[:] = sorted(nums1[:m]+nums2)
#         return nums1

# class Solution:
#     def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
#         """
#         Do not return anything, modify nums1 in-place instead.
#         """
#         nums1_copy = nums1[:m]
#         nums1[:] = []
#         p1, p2 = 0, 0
#         while p1 < m and p2 < n:
#             if nums1_copy[p1] < nums2[p2]:
#                 nums1.append(nums1_copy[p1])
#                 p1 += 1
#             else:
#                 nums1.append(nums2[p2])
#                 p2 += 1
        
#         if p1 < m:
#             nums1[p1 + p2:] = nums1_copy[p1:]
#         if p2 < n:
#             nums1[p1 + p2:] = nums2[p2:]

# @lc code=end


# 排序法, nums1[:]可以在原内存上进行修改
# 双指针
# 双指针 从nums1尾部开始填写, 从大到小