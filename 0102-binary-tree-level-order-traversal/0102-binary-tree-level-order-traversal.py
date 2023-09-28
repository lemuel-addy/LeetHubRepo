# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        # if not root:
        #     return []
        
        # queue = deque([root])
        # answer = [[root.val]]

        # while queue:
        #     node = queue.popleft()
        #     ans = []
        #     if node.left:
        #         ans.append(node.left.val)
        #         queue.append(node.left)
        #     if node.right:
        #         ans.append(node.right.val)
        #         queue.append(node.right)
        #     if ans != []:
        #         answer.append(ans)
        # return answer

        res= []
        q = deque()
        q.append(root)

        while q:
            lth = len(q)
            level = []
            for i in range(lth):
                node = q.popleft()
                if node:
                    level.append(node.val)
                    q.append(node.left)
                    q.append(node.right)
            if level:
                res.append(level)
        return res

        
            

