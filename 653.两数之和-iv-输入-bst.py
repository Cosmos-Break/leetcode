#
# @lc app=leetcode.cn id=653 lang=python3
#
# [653] 两数之和 IV - 输入 BST
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTarget(self, root: TreeNode, k: int) -> bool:
        val_set = set()
        def dfs(node):
            if node is None:
                return False
            if k - node.val in val_set:
                return True
            else:
                val_set.add(node.val)
                return dfs(node.left) or dfs(node.right)
        return dfs(root)

# @lc code=end

