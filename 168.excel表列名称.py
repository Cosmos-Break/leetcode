#
# @lc app=leetcode.cn id=168 lang=python3
#
# [168] Excel表列名称
#

# @lc code=start
class Solution:
    def convertToTitle(self, n: int) -> str:
        capitals = [chr(x) for x in range(ord('A'), ord('Z')+1)]
        m = n
        result = ''
        while m != 0:
            k = (m-1) % 26
            result += capitals[k]
            m = (m-1) // 26
        return result[::-1]
# @lc code=end

