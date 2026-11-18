# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        output = []

        def levelTraversal(node, h):
            if not node:
                return None
            if len(output) == h:
                output.append([])
            output[h].append(node.val)
            levelTraversal(node.left, h + 1)
            levelTraversal(node.right, h + 1)

        levelTraversal(root, 0)
        return output