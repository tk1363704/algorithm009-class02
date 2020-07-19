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

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # My solution.
    def buildTree(self, preorder, inorder) -> TreeNode:
        if len(preorder) == 0 or len(inorder) == 0:
            return None
        def helper(preorder, inorder):
            if len(preorder) == 1 and len(inorder) == 1 and preorder[0] == inorder[0]:
                node = TreeNode(preorder[0])
                return node
            if len(preorder) == 0 or len(inorder) == 0:
                return None
            i = 0
            while i < len(inorder):
                if inorder[i] == preorder[0]:
                    break
                i += 1
            root = TreeNode(inorder[i])
            if i == len(inorder) - 1:
                right_inorder = []
            else:
                right_inorder = inorder[i+1:]
            if i == 0:
                left_inorder = []
            else:
                left_inorder = inorder[0:i]
            root.left = helper(preorder[1:1+len(left_inorder)], left_inorder)
            root.right = helper(preorder[1+len(left_inorder):], right_inorder)
            return root
        return helper(preorder, inorder)

    def dfs(self, root):
        if not root:
            return None
        print(root.val)
        self.dfs(root.left)
        self.dfs(root.right)

    # Recursion: not divide array.
    def buildTree_improved(self, preorder, inorder) -> TreeNode:
        def helper(preleft, preright, inleft, inright):
            # Note: This judging condition is very important!
            # It can also solve the empty array problem!
            if preleft > preright:
                return None

            inorder_root_index = inhash[preorder[preleft]]
            len_left_inorder = inorder_root_index - inleft
            root = TreeNode(preorder[preleft])

            root.left = helper(preleft + 1, preleft + len_left_inorder, inleft, inorder_root_index - 1)
            root.right = helper(preleft + len_left_inorder + 1, preright, inorder_root_index + 1, inright)
            return root

        inhash = {e: i for i, e in enumerate(inorder)}
        n = len(inorder)
        return helper(0, n - 1, 0, n - 1)

if __name__=="__main__":
    solution = Solution()
    solution.dfs(solution.buildTree_improved([3, 9, 20, 15, 7], [9, 3, 15, 20, 7]))
