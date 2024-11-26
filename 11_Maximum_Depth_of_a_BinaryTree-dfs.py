class Solution(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        
        if root is None:
            return 0
        
        # Recursive dfs
        left_depth = self.maxDepth(root.left)
        right_depth = self.maxDepth(root.right)
       
        # Return the maximum depth plus 1 (for the current node)
        return 1 + max(left_depth, right_depth)
