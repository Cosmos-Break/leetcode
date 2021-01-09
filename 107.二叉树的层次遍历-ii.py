#
# @lc app=leetcode.cn id=107 lang=python3
#
# [107] 二叉树的层次遍历 II
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def levelOrderBottom(self, root: TreeNode) -> List[List[int]]:
        result = []
        def dfs(root, level, result):
            if root is None:
                return
            else:
                if len(result) < level + 1:
                    result.append([])
                result[level].append(root.val)
                dfs(root.left, level + 1, result)
                dfs(root.right, level + 1, result)
        dfs(root, 0, result)
        return result[::-1]
# @lc code=end

