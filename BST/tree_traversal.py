class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def bfs_list(root):
    if not root:
        return []

    queue = [root]  # start with root
    result = []

    while queue:
        node = queue.pop(0)  # dequeue
        result.append(node.val)

        if node.left:
            queue.append(node.left)  # enqueue
        if node.right:
            queue.append(node.right)  # enqueue

    return result

# proper Queue impl
def bfs(root):
    if not root:
        return []

    result = []
    queue = deque([root])

    while queue:
        node = queue.popleft()
        result.append(node.val)

        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)

    return result

def dfs_preorder(root):
    if not root:
        return []
    return [root.val] + dfs_preorder(root.left) + dfs_preorder(root.right)

def dfs_inorder(root):
    if not root:
        return []
    return dfs_inorder(root.left) + [root.val] + dfs_inorder(root.right)

def dfs_postorder(root):
    if not root:
        return []
    return dfs_postorder(root.left) + dfs_postorder(root.right) + [root.val]