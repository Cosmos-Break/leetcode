#
# @lc app=leetcode.cn id=989 lang=python3
#
# [989] 数组形式的整数加法
#

# @lc code=start
# class Solution:
#     def addToArrayForm(self, A: List[int], K: int) -> List[int]:
#         a = int(''.join([str(char) for char in A]))
#         return list(str(a + K))

class Solution:
    def addToArrayForm(self, A: List[int], K: int) -> List[int]:
        ans = []
        for a in A[::-1]:
            sum = a + K%10
            K //= 10
            if sum >= 10:
                K += 1
                sum -= 10
            ans.append(sum)
        while K > 0:
            ans.append(K%10)
            K //= 10
        return ans[::-1]
        
# @lc code=end

