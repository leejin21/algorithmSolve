# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# 76 ms
class Solution:
    
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        # 백트래킹
        '''
        상태 값 리턴 및 누적
        지름 값(=answer) 업데이트
        '''
        self.diameter = 0
        def dfs(node: Optional[TreeNode]) -> int:
            # TODO 종료조건
            if not node:
                return -1
            
            left = dfs(node.left)
            right = dfs(node.right)
            
            self.diameter = max(self.diameter, left+right+2)
            return max(left, right)+1
        
        dfs(root)
        return self.diameter