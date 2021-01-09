#
# @lc app=leetcode.cn id=111 lang=python3
#
# [111] 二叉树的最小深度
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def minDepth(self, root: TreeNode) -> int:
        if root is None:
            return 0
        queue = []
        queue.append((root, 1))
        while queue:
            node, level = queue.pop(0)
            if node.left is None and node.right is None:
                return level
            if node.left is not None:
                queue.append((node.left, level + 1))
            if node.right is not None:
                queue.append((node.right, level + 1))
# @lc code=end
# if __name__ == "__main__":
#     s = Solution()
#     node1 = TreeNode(1)
#     node2 = TreeNode(2)
#     node3 = TreeNode(3)
#     node1.left = node2
#     node1.right = node3
#     s.minDepth(node1)
