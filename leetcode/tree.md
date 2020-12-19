+ [Maximum Depth of Binary Tree](#maximum-depth-of-binary-tree)
+ [Binary Tree Inorder Traversal](#binary-tree-inorder-traversal)
+ [Invert a Binary Tree](#invert-a-binary-tree)
+ [Binary Search Tree Iterator](#binary-search-tree-iterator)
+ [Binary Tree Level Order Traversal](#binary-tree-level-order-traversal)
+ [Kth Smallest Element in a BST](#kth-smallest-element-in-a-bst)
+ [Validate Binary Search Tree](#validate-binary-search-tree)
+ [Symmetric Tree](#symmetric-tree)
## Maximum Depth of Binary Tree
https://leetcode.com/problems/maximum-depth-of-binary-tree/
```python
class Solution:
    def maximumDepth(self, root: TreeNode) -> int:
        if root is None:
            return 0
        leftN = self.maxDepth(root.left)
        rightN = self.maxDepth(root.right)
        return max(leftN,rightN) + 1
```
## Binary Tree Inorder Traversal
https://leetcode.com/problems/binary-tree-inorder-traversal/
```python
class Solution:
    def InorderTraversal(self, root: TreeNode) -> List[int]:
        nodes = []
        def traverse(root):
            if root:
                traverse(root.left)
                nodes.append(root.val)
                traverse(root.right)
        traverse(root)

        return nodes
```
## Invert a Binary Tree
https://leetcode.com/problems/invert-binary-tree/
```python
class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        return self.invert(root)


    def invert(self,node):
        if node is None:
            return
        node.left, node.right = node.right, node.left
        self.invert(node.left)
        self.invert(node.right)
        return node
```
## Binary Search Tree Iterator
https://leetcode.com/problems/binary-search-tree-
```python
class BSTIterator:
    def __init__(self, root: TreeNode):
        self.stack = []
        while root:
            self.stack.append(root)
            root = root.left

    def next(self) -> int:

        ans = self.stack.pop()
        root = ans
        root = root.right        
        if root:
            while root:
                self.stack.append(root)
                root = root.left

        return ans.val

    def hasNext(self) -> bool:
        return self.stack != []
```
## Binary Tree Level Order Traversal
https://leetcode.com/problems/binary-tree-level-order-traversal/
```python
class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        res = []
        def solve(node, depth=0):
            if node:
                if depth >= len(res):
                    res.append([])
                solve(node.left, depth+1)
                res[depth].append(node.val)
                solve(node.right, depth+1)
        solve(root)
        return res
```
## Kth Smallest Element in a BST
https://leetcode.com/problems/kth-smallest-element-in-a-bst/
```python
class Solution:
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        def inorder(root):
            if root is None:
                return []
            return inorder(root.left) + [root.val]  + inorder(root.right)

        ans = inorder(root)
        return ans[k-1]
```
## Validate Binary Search Tree
 https://leetcode.com/problems/validate-binary-search-tree/
 ```python
 def isValidBST(self, root: TreeNode) -> bool:
        self.answer = True

        def dfs(root, left, right):
            if root:
                if left >= root.val or root.val >= right:
                    self.answer = False
                    return
                dfs(root.left, left, root.val)
                dfs(root.right, root.val, right)
        dfs(root, float("-inf"), float('inf'))
        return self.answer
```
## Symmetric Tree
https://leetcode.com/problems/symmetric-tree/
```python
class Solution:
    def isSymmetric(self, root):
        stack = []
        if root:
            stack.append([root.left, root.right])
        while(len(stack) > 0):
            left, right = stack.pop()

            if left and right:
                if left.val != right.val: return False
                stack.append([left.left, right.right])
                stack.append([right.left, left.right])

            elif left or right: return False

        return True
```
