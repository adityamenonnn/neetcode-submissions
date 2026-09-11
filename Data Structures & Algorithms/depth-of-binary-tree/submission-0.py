# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:

        if not root:
            return 0 
        
        #recursive
        '''
        return 1 + max(self.maxDepth(root.right),self.maxDepth(root.left))
        '''

        #iterative BFS will have a deque
        '''
        level = 0
        q = deque()
        q.append(root)
        while q:
            #now for each level thast why th efor loop is there
            for i in range(len(q)):
                node = q.pop()
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            level += 1
        return level
        '''

        #Iterative BFS
        
        stack  = [(root,1)]
        res = 1
        while stack:
            node,depth = stack.pop()
            res = max(res,depth)
            if node.right:
                stack.append((node.right,depth+1))
            if node.left:
                stack.append((node.left,depth+1))
        return res

