#
# @lc app=leetcode.cn id=944 lang=python3
#
# [944] 删列造序
#

# @lc code=start
class Solution(object):
    def minDeletionSize(self, A):
        ans = 0
        for col in zip(*A):
            if any(col[i] > col[i+1] for i in range(len(col) - 1)):
                ans += 1
        return ans

# @lc code=end

