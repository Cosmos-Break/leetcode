#
# @lc app=leetcode.cn id=1033 lang=python3
#
# [1033] 移动石子直到连续
#

# @lc code=start
class Solution:
    def numMovesStones(self, a: int, b: int, c: int) -> List[int]:
        x,y,z=sorted([a,b,c])
        if x+1==y and y+1==z:       #三连续
            return [0,0]
        if x+1<y and y+1==z:        #右连续
            return [1,y-x-1]
        if x+1==y and y+1<z:        #左连续
            return [1,z-y-1]
        if x+2==y or y+2==z:        #左边两数相差2，或者右边两数相差2
            return [1,z-x-2]
        if x+1<y and y+1<z:
            return [2,z-x-2]

# @lc code=end

