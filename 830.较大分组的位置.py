#
# @lc app=leetcode.cn id=830 lang=python3
#
# [830] 较大分组的位置
#

# @lc code=start
class Solution:
    def largeGroupPositions(self, s: str) -> List[List[int]]:
        ret = list()
        n, num = len(s), 1

        for i in range(n):
            if i == n - 1 or s[i] != s[i + 1]:
                if num >= 3:
                    ret.append([i - num + 1, i])
                num = 1
            else:
                num += 1
        
        return ret
# @lc code=end

