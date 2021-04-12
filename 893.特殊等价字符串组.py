#
# @lc app=leetcode.cn id=893 lang=python3
#
# [893] 特殊等价字符串组
#

# @lc code=start
class Solution(object):
    def numSpecialEquivGroups(self, A):
        def count(A):
            ans = [0] * 52
            for i, letter in enumerate(A):
                ans[ord(letter) - ord('a') + 26 * (i%2)] += 1
            return tuple(ans)

        return len({count(word) for word in A})

# @lc code=end

