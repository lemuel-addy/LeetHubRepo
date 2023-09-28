# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not root and not subRoot:
            return True
        if not root or not subRoot:
            return False
        if self.sameTree(root,subRoot):
            return True
     
        return self.isSubtree(root.right,subRoot) or self.isSubtree(root.left,subRoot)
        
        

    def sameTree( self, p,q):
        if not p and not q:
            return True
        if not p or not q:
            return False
        if p.val != q.val:
            return False
        
        return self.sameTree(p.left,q.left) and self.sameTree(p.right,q.right)
