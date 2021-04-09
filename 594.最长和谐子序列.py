#
# @lc app=leetcode.cn id=594 lang=python3
#
# [594] 最长和谐子序列
#

# @lc code=start
class Solution:
    def findLHS(self, nums: List[int]) -> int:
        cnt_dict = Counter(nums)
        ret = 0
        for key in cnt_dict:
            if key + 1 in cnt_dict:
               ret = max(ret, cnt_dict[key] + cnt_dict[key+1]) 
        return ret
# @lc code=end

