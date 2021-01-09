#
# @lc app=leetcode.cn id=88 lang=python3
#
# [88] 合并两个有序数组
#
from typing import List
# @lc code=start
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        if m == 0:
            j = 0
            while j < len(nums2):
                nums1[j] = nums2[j]
                j += 1
        i = m - 1
        j = n - 1
        k = m + n - 1
        while i >= 0 and j >= 0:
            if nums2[j] > nums1[i]:
                nums1[k] = nums2[j]
                k -= 1
                j -= 1
            else:
                nums1[k] = nums1[i]
                k -= 1
                i -= 1
        nums1[:j + 1] = nums2[:j + 1]

# @lc code=end
if __name__ == "__main__":
    s = Solution()
    # s.merge([2, 0], 1, [1], 1)
    # s.merge([1, 2, 3, 0, 0, 0], 3, [2, 5, 6], 3)
    s.merge([4,0,0,0,0,0], 1, [1,2,3,5,6], 5)
