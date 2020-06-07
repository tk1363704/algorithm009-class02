# 105. Construct Binary Tree from Preorder and Inorder Traversal
# Given preorder and inorder traversal of a tree, construct the binary tree.
#
# Note:
# You may assume that duplicates do not exist in the tree.
#
# For example, given
#
# preorder = [3,9,20,15,7]
# inorder = [9,3,15,20,7]
# Return the following binary tree:
#
#     3
#    / \
#   9  20
#     /  \
#    15   7

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # # My solution.
    # def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
    #     if len(preorder) == 0 or len(inorder) == 0:
    #         return None
    #     def helper(preorder, inorder):
    #         if len(preorder) == 1 and len(inorder) == 1 and preorder[0] == inorder[0]:
    #             node = TreeNode(preorder[0])
    #             return node
    #         index = -1
    #         for i in range(len(inorder)):
    #             if inorder[i] == preorder[0]:
    #                 index = i
    #                 break
    #         root = TreeNode(inorder[index])
    #         root.left = helper(preorder[1:1+len(inorder[0:index])], inorder[0:index])
    #         root.right = helper(preorder[1+len(inorder[0:index]):], inorder[index+1:])
    #         return root
    #     return helper(preorder, inorder)

    # My solution.
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        if not preorder or not inorder:  # 递归终止条件
            return
        root = TreeNode(preorder[0])  # 先序为“根左右”，所以根据preorder可以确定root
        idx = inorder.index(preorder[0])  # 中序为“左根右”，根据root可以划分出左右子树
        # 下面递归对root的左右子树求解即可
        root.left = self.buildTree(preorder[1:1 + idx], inorder[:idx])
        root.right = self.buildTree(preorder[1 + idx:], inorder[idx + 1:])
        return root