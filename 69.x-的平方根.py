#
# @lc app=leetcode.cn id=69 lang=python3
#
# [69] x 的平方根
#

# @lc code=start
class Solution:
    def mySqrt(self, x: int) -> int:
        l = 0
        r = x
        while l <= r:
            mid = l + (r - l) // 2
            if mid * mid <= x and x < (mid + 1) * (mid + 1):
                return mid
            elif mid * mid > x:
                r = mid
            else:
                l = mid + 1

            
# @lc code=end
if __name__ == "__main__":
    s = Solution()
    print(s.mySqrt(1))
