#
# @lc app=leetcode.cn id=589 lang=python3
#
# [589] N 叉树的前序遍历
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
    def preorder(self, root: 'Node') -> List[int]:
        self.ret = []
        def dfs(node):
            if node is None:
                return
            self.ret.append(node.val)
            for child in node.children:
                dfs(child)
        dfs(root)
        return self.ret
# @lc code=end

