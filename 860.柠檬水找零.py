# @before-stub-for-debug-begin
from python3problem860 import *
from typing import *
# @before-stub-for-debug-end

#
# @lc app=leetcode.cn id=860 lang=python3
#
# [860] 柠檬水找零
#

# @lc code=start
class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        fives = 0
        tens = 0
        for bill in bills:
            if bill == 5:
                fives += 1
            elif bill == 10:
                if fives > 0:
                    fives -= 1
                    tens += 1
                else:
                    return False
            elif bill == 20 :
                if tens > 0 and fives > 0 :
                    tens -= 1
                    fives -= 1
                elif fives > 2:
                    fives -= 3
                else:
                    return False
        return True
# @lc code=end

