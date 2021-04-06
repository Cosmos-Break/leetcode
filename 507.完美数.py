#
# @lc app=leetcode.cn id=507 lang=python3
#
# [507] 完美数
#

# @lc code=start
class Solution:
    def checkPerfectNumber(self, num: int) -> bool:
        #对于数字1:直接返回`False`
        if num == 1:
            return False
        #计数从1开始
        total = 1
        #我们只需要判断`2-int(sqrt(num))+1`的数，全部累加
        for i in range(2, int(math.sqrt(num)) + 1):
            if num % i == 0:
                #这里total要加上i和num // i
                total += (i + num // i)
        return total == num
        
# @lc code=end

