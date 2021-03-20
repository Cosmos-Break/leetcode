#
# @lc app=leetcode.cn id=219 lang=python3
#
# [219] 存在重复元素 II
#

# @lc code=start
class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        s = set()
        for i in range(len(nums)):
            if nums[i] in s:
                return True
            s.add(nums[i])
            if len(s) > k:
                s.remove(nums[i-k])
        return False
# @lc code=end

