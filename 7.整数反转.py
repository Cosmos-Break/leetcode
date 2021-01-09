#
# @lc app=leetcode.cn id=7 lang=python3
#
# [7] 整数反转
#

# @lc code=start
# class Solution:
#     def reverse(self, x: int) -> int:
#         reversed_list = list(str(x))
#         reversed_list.reverse()
#         if reversed_list[-1] == '-':
#             reversed_list.pop(-1)
#             reversed_list.insert(0, '-')
#         result = int(''.join(reversed_list))
#         if result > pow(-2, 31) and result < (pow(2, 31) - 1):
#             return result
#         else:
#             return 0
class Solution:
    def reverse(self, x: int) -> int:
        x = str(x)
        if x[0] != '-':
            x = x[::-1]
        else:
            x = x[:0:-1]
            x = '-'+str(x)
        x = int(x)
        if pow(-2, 31) <= x <= pow(2,31)-1:
            return x
        else:
            return 0
# @lc code=end
# [::-1]是让str从后往前读取, 实现翻转字符串
# [2::-1]是让str从index 2开始, 从index 2往前读到index 0
# [:2:-1]是从最后开始读到index 2, index2不包含
# 判断是否是负数,如果是负数则 去掉符号进行翻转, 翻转完成之后再去掉
# 最后判断int是否溢出