#
# @lc app=leetcode.cn id=868 lang=python3
#
# [868] 二进制间距
#

# @lc code=start
class Solution(object):
    def binaryGap(self, N):
        last = None
        ans = 0
        for i in range(32):
            if (N >> i) & 1:
                if last is not None:
                    ans = max(ans, i - last)
                last = i
        return ans

# @lc code=end

