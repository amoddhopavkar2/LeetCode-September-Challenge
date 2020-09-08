# Sum of Root to Leaf Binary Numbers

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumRootToLeaf(self, root: TreeNode) -> int:
        def traversal(root, path, path_len, all_paths):
            if not root:
                return
            if len(path) > path_len:
                path[path_len] = root.val
            else:
                path.append(root.val)

            path_len += 1
            if not root.left and not root.right:
                all_paths.append(int(''.join(str(val)
                                             for val in path[:path_len]), 2))
            else:
                traversal(root.left, path, path_len, all_paths)
                traversal(root.right, path, path_len, all_paths)

        path = []
        traversal(root, [], 0, path)
        return sum(path)
