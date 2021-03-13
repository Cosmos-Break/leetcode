# @before-stub-for-debug-begin
from python3problem898 import *
from typing import *
# @before-stub-for-debug-end

#
# @lc app=leetcode.cn id=898 lang=python3
#
# [898] 子数组按位或操作
#

# @lc code=start
class Solution:
    def subarrayBitwiseORs(self, arr: List[int]) -> int:
        ans = set()
        cur = {0}
        for x in arr:
            cur = {x | y for y in cur} | {x}
            ans |= cur
        return len(ans)

        # ret = set()
        # i, j = 0, 0
        
        # for i in range(len(arr)):
        #     or_val = arr[i]
        #     for j in range(i, len(arr)):
        #         or_val = or_val | arr[j]
        #         ret.add(or_val)

        # return len(ret)
# @lc code=end

