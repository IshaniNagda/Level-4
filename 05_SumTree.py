class Solution:
    def sum(self, root):
        if root is None:
            return 0
        
        return self.sum(root.left) + root.data + self.sum(root.right)
        
    
    
    
    def isSumTree(self,root):
        if root is None or (root.left is None and root.right is None):
            return 1
        
        lsum= self.sum(root.left)
        rsum= self.sum(root.right)
        
        if (root.data == lsum + rsum) and self.isSumTree(root.left) and self.isSumTree(root.right):
            return 1
        return 0
