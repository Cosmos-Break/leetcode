#
# @lc app=leetcode.cn id=590 lang=python3
#
# [590] N 叉树的后序遍历
#

# @lc code=start
"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        self.ret = []
        def dfs(node):
            if node is None:
                return
            for child in node.children:
                dfs(child)
            self.ret.append(node.val)
        dfs(root)
        return self.ret
# @lc code=end

