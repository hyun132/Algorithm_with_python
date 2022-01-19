# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

#제일 효율이 좋은 것(전역변수를 하나 두고 각 노드의 left와 right index 범위만 제한.)
class Solution1: 
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        inorder_index=dict()
        
        for index, num in enumerate(inorder):
            inorder_index[num] = index
        
        pre_index = 0
        
        def solution(left_index,right_index):
            nonlocal pre_index
            
            if left_index>right_index: return None

            node = TreeNode(preorder[pre_index])
            index = inorder_index[node.val]

            pre_index +=1
            
            node.left = solution(left_index,index-1)
            node.right = solution(index+1,right_index)
            
            return node

        return solution(0,len(inorder)-1)
        
# 각 리스트를 범위에 맞게 잘라서 넘겨준다. (처음 푼 방법)
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if len(preorder)<1 : return None
        if len(preorder)==1 : return TreeNode(preorder[0])
        
        node = TreeNode(preorder[0])
        index = inorder.index(preorder[0])
        
        node.left = self.buildTree(preorder[1:index+1],inorder[:index])
        node.right = self.buildTree(preorder[index+1:],inorder[index+1:])
        
        return node
