class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.height = 1  # required for AVL balancing

# Utility: get height
def height(node):
    return node.height if node else 0

# Utility: balance factor
def get_balance(node):
    return height(node.left) - height(node.right) if node else 0

# Right rotation
def right_rotate(y):
    x = y.left
    T2 = x.right

    # rotation
    x.right = y
    y.left = T2

    # update heights
    y.height = 1 + max(height(y.left), height(y.right))
    x.height = 1 + max(height(x.left), height(x.right))
    return x

# Left rotation
def left_rotate(x):
    y = x.right
    T2 = y.left

    # rotation
    y.left = x
    x.right = T2

    # update heights
    x.height = 1 + max(height(x.left), height(x.right))
    y.height = 1 + max(height(y.left), height(y.right))
    return y

# Insert node
def insert(root, key):
    if not root:
        return Node(key)
    if key < root.val:
        root.left = insert(root.left, key)
    else:
        root.right = insert(root.right, key)

    # update height
    root.height = 1 + max(height(root.left), height(root.right))

    # check balance
    balance = get_balance(root)

    # Left Left
    # "We're left-heavy AND the key went to the left of the left child"
    if balance > 1 and key < root.left.val:
        return right_rotate(root)
    # Right Right
    if balance < -1 and key > root.right.val:
        return left_rotate(root)
    # Left Right
    if balance > 1 and key > root.left.val:
        root.left = left_rotate(root.left)
        return right_rotate(root)
    # Right Left
    if balance < -1 and key < root.right.val:
        root.right = right_rotate(root.right)
        return left_rotate(root)

    return root

# Inorder traversal
def inorder(root):
    if root:
        inorder(root.left)
        print(root.val, end=" ")
        inorder(root.right)

# Search
def search(root, key):
    if not root or root.val == key:
        return root
    return search(root.left, key) if key < root.val else search(root.right, key)

# Find min (used in delete)
def find_min(node):
    while node.left:
        node = node.left
    return node

# Delete node
def delete(root, key):
    if not root:
        return root
    if key < root.val:
        root.left = delete(root.left, key)
    elif key > root.val:
        root.right = delete(root.right, key)
    else:
        # Node with one or no child
        if not root.left:
            return root.right
        elif not root.right:
            return root.left
        # Node with two children
        temp = find_min(root.right)
        root.val = temp.val
        root.right = delete(root.right, temp.val)

    # Update height
    root.height = 1 + max(height(root.left), height(root.right))

    # Balance
    balance = get_balance(root)
    # Left Left
    # "We're left-heavy AND the left child is left-heavy"
    if balance > 1 and get_balance(root.left) >= 0:
        return right_rotate(root)
    # Left Right
    if balance > 1 and get_balance(root.left) < 0:
        root.left = left_rotate(root.left)
        return right_rotate(root)
    # Right Right
    if balance < -1 and get_balance(root.right) <= 0:
        return left_rotate(root)
    # Right Left
    if balance < -1 and get_balance(root.right) > 0:
        root.right = right_rotate(root.right)
        return left_rotate(root)

    return root

# ✅ Example usage
if __name__ == "__main__":
    root = None
    for key in [10, 20, 30, 40, 50, 25]:
        root = insert(root, key)

    print("Inorder traversal of AVL tree:")
    inorder(root)  # Should print sorted order
    print()

    print("Deleting 20...")
    root = delete(root, 20)
    inorder(root)
    print()

    print("Searching for 30:", "Found" if search(root, 30) else "Not found")