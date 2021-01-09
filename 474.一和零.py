#
# @lc app=leetcode.cn id=474 lang=python3
#
# [474] 一和零
#

# @lc code=start
class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        if len(strs) == 0:
            return 0
        
        dp = [[0]*(n+1) for _ in range(m+1)]   #准备很多个背包
        
        for strs_item in strs:
            item_count0 = strs_item.count('0')
            item_count1 = strs_item.count('1')
            
            #遍历可容纳的背包 
            for i in range(m, item_count0 - 1, -1):  #采取倒序
                for j in range(n, item_count1 - 1, -1):
                    dp[i][j] = max(dp[i][j], 1 + dp[i-item_count0][j-item_count1])
                    
        return dp[m][n] 


# @lc code=end
if __name__ == "__main__":
    s = Solution()
    s.findMaxForm(["10","0001","111001","1","0"], 5, 3)


# [0, 0, 0, 0]
# [0, 1, 1, 1]
# [0, 1, 1, 1]
# [0, 1, 1, 1]
# [0, 1, 1, 1]
# [0, 1, 1, 1]


# [0, 0, 0, 0]
# [0, 1, 1, 1]
# [0, 1, 1, 1]
# [0, 1, 1, 1]
# [0, 1, 2, 2]
# [0, 1, 2, 2]


# [0, 0, 0, 0]
# [0, 1, 1, 1]
# [0, 1, 1, 1]
# [0, 1, 1, 1]
# [0, 1, 2, 2]
# [0, 1, 2, 2]


# [0, 1, 1, 1]
# [0, 1, 2, 2]
# [0, 1, 2, 2]
# [0, 1, 2, 2]
# [0, 1, 2, 3]
# [0, 1, 2, 3]


# [0, 1, 1, 1]
# [1, 2, 2, 2]
# [1, 2, 3, 3]
# [1, 2, 3, 3]
# [1, 2, 3, 3]
# [1, 2, 3, 4]