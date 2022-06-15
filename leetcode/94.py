# 94. Binary Tree Inorder Traversal
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        # LMR
        # preorder 로 주어졌을 때 inorder로 뽑기
        
        self.output = []
        # 일단 그래프 만들자: 만들 때는 MLR
        def recursion(cur):
            
            if cur.left:
                recursion(cur.left)
                
            self.output.append(cur.val)
                
            if cur.right:
                recursion(cur.right)
                
        
        if root: recursion(root)
        # print(root)
        return self.output
        
