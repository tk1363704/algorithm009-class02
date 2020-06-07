# 236. Lowest Common Ancestor of a Binary Tree
# Given a binary tree, find the lowest common ancestor (LCA) of two given nodes in the tree.
#
# According to the definition of LCA on Wikipedia: “The lowest common ancestor is defined between two nodes p and q as the lowest node in T that has both p and q as descendants (where we allow a node to be a descendant of itself).”
#
# Given the following binary tree:  root = [3,5,1,6,2,0,8,null,null,7,4]
# Example 1:
#
# Input: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 1
# Output: 3
# Explanation: The LCA of nodes 5 and 1 is 3.

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    answer = None
    parent_hash = {}

    # Recursion.
    # def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
    #     def helper(root, p, q):
    #         if not root:
    #             return False
    #         left_flag = helper(root.left, p, q)
    #         right_flag = helper(root.right, p, q)
    #         # If the left_flag and right_flag are both True,
    #         # then p and q must be located in different branches of the root node.
    #         if (left_flag and right_flag) or ((root.val == p.val or root.val == q.val) and (left_flag or right_flag)):
    #             self.answer = root
    #         return root.val == p.val or root.val == q.val or left_flag or right_flag
    #     helper(root, p, q)
    #     return self.answer

    # Store parent node.
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        self.parent_hash[root] = None

        def helper(self, root):
            if root.left:
                self.parent_hash[root.left] = root
                helper(self, root.left)
            if root.right:
                self.parent_hash[root.right] = root
                helper(self, root.right)

        helper(self, root)
        visited_list = {}
        # Note this! Add itself into the visited list.
        while p:
            visited_list[p] = True
            p = self.parent_hash[p]
        while q:
            if q in visited_list:
                return q
            q = self.parent_hash[q]
        return None