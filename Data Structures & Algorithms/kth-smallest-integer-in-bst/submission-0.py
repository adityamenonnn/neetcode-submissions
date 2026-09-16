class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        c = 0
        res = None

        def dfs(node):
            nonlocal c,res
            if not node:
                return

            dfs(node.left)

            c += 1                  # visiting this node
            if c == k:
                res = node.val
                return

            dfs(node.right)

        dfs(root)
        return res