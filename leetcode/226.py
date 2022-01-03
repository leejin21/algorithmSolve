# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

import collections

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        # BFS solution: 26ms
        '''
        q에서 root 빼고 그의 left, right를 바꿔준다.
        바꿔준 left, right에 대해 q에 넣고 동일 반복.
        None의 경우 무시
        
        종결 조건: q의 길이가 0이 될 때까지
        '''
        q = collections.deque([root])
        
        while(q):
            node = q.popleft()
            if node:
                node.left, node.right = node.right, node.left
                q.append(node.left)
                q.append(node.right)
                
        return root
        
        # pythonic solution: 72ms
#         if root:
#             root.left, root.right = self.invertTree(root.right), self.invertTree(root.left)
#             return root
        
#         return None