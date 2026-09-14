# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        max_heigh_diff = 0 

        def dfs(root):
            if not root:
                return 0
            
            left = dfs(root.left)
            right = dfs(root.right)

            nonlocal max_heigh_diff
            max_heigh_diff = max(max_heigh_diff, abs(left - right))

            return 1 + max(left,right)
        
        dfs(root)
        return max_heigh_diff<=1