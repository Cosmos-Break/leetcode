# @before-stub-for-debug-begin
from python3problem6 import *
from typing import *
# @before-stub-for-debug-end

#
# @lc app=leetcode.cn id=6 lang=python3
#
# [6] Z 字形变换
#

# @lc code=start
class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s
        curRow = 0
        goingDown = True
        rows = [[] for i in range(min(numRows, len(s)))]
        for char in s:
            rows[curRow].append(char)
            curRow += 1 if goingDown else -1
            if curRow == 0 or curRow == numRows - 1:
                goingDown = not goingDown
        ret = []
        for row in rows:
            ret += row
        return ''.join(ret)

# @lc code=end

# 每行都用一个数组来表示，遍历字符串s，用goingDown标记是否往下走，当curRow当前行为0或者当前行等于numRows的时候转变方向。