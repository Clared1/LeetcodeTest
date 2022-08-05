from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def addOneRow(self, root: Optional[TreeNode], val: int, depth: int) -> Optional[TreeNode]:
        if depth == 1:
            tmp = TreeNode(val)
            tmp.left = root
            return tmp
        tmp = [root]
        depth-=2
        while(depth):
            tmptmp = []
            for i in tmp:
                if i.left:
                    tmptmp.append(i.left)
                if i.right:
                    tmptmp.append(i.right)
            tmp = tmptmp
            depth-=1
        for i in tmp:
            tmptmp = i.left
            i.left = TreeNode(val)
            i.left.left = tmptmp
            tmptmp = i.right
            i.right = TreeNode(val)
            i.right.right = tmptmp
        return root