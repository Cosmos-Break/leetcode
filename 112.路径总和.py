#
# @lc app=leetcode.cn id=112 lang=python3
#
# [112] 路径总和
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def hasPathSum(self, root: TreeNode, sum: int) -> bool:
        if root is None:
            return False
        queue = []
        queue.append((root, root.val))
        while queue:
            node, sum_now = queue.pop(0)
            if sum_now == sum and node.left is None and node.right is None:
                return True
            if node.left is not None:
                queue.append((node.left, sum_now + node.left.val))
            if node.right is not None:
                queue.append((node.right, sum_now + node.right.val))
        return False
# @lc code=end

