#
# @lc app=leetcode.cn id=501 lang=python3
#
# [501] 二叉搜索树中的众数
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findMode(self, root: TreeNode) -> List[int]:
        base = float("inf")
        count, maxCount = 0, 0
        ans = []
        def update(x):
            nonlocal base, count, maxCount, ans
            if x == base:
                count += 1
            else:
                count = 1
                base = x
            if count == maxCount:
                ans.append(x)
            elif count > maxCount:
                ans = [x]
                maxCount = count
        def dfs(node):
            if node is None:
                return
            dfs(node.left)
            update(node.val)
            dfs(node.right)
        
        dfs(root)
        return ans

# @lc code=end

