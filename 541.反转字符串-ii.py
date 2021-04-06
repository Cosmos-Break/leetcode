#
# @lc app=leetcode.cn id=541 lang=python3
#
# [541] 反转字符串 II
#

# @lc code=start
class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        n=len(s)
        arr=list(s)
        for i in range(0,n,2*k):
            arr[i:i+k]=arr[i:i+k][::-1]
        return "".join(arr)

# @lc code=end

