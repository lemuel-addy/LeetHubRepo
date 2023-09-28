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
        
        #Recursive Approach with Depth First Search
        # return 1 + max(self.maxDepth(root.left),self.maxDepth(root.right))

        #Base First Search Approach
        # level = 0
        # q = deque([root])
        # while q:
        #     for i in range(len(q)):
        #         node = q.popleft()
        #         if node.right:
        #             q.append(node.right)
        #         if node.left:
        #             q.append(node.left)
        #     level += 1
        # return level


        #Iterative DSF approach
        stack = [[root,1]]
        res = 1
        while stack:
            node,depth = stack.pop()
            if node:
                res=max(res,depth)
                stack.append([node.left,depth+1])
                stack.append([node.right,depth+1])
                
        return res




                
        