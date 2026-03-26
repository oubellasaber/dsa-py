class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def insert(root, val):
    if root is None:
        return Node(val)
    
    if val < root.val:
        root.left = insert(root.left, val)
    else:
        root.right = insert(root.right, val)

    return root

def search(root, val):
    if root is None or root.val == val:
        return root

    if val < root.val:
        return search(root.left, val)
    elif val > root.val:
        return search(root.right, val)

# Le successeur d’un nœud X est le nœud possédant la plus petite étiquette supérieure à l’étiquette de X.
# Le prédécesseur d’un nœud X est le nœud possédant la plus grande étiquette inférieure à l’ étiquette de X.

def find_min(root):
    while root and root.left:
        root = root.left
    return root

def find_max(root):
    while root and root.right:
        root = root.right
    return root

def delete(root, val):
    if root is None:
        return None

    if val < root.val:
        root.left = delete(root.left, val)
    elif val > root.val:
        root.right = delete(root.right, val)
    else:
        # No child or one child
        if root.left is None:
            return root.right
        elif root.right is None:
            return root.left

        # Two children
        # Replace with a value that is “next in sorted order”
        
        # Successor
        succ = find_min(root.right)
        root.val = succ.val
        root.right = delete(root.right, succ.val)

        # Predecessor
        # pred = find_max(root.left)
        # root.val = pred.val
        # root.left = delete(root.left, pred.val)

    return root
        

def inorder(root):
    if not root:
        return []
    return inorder(root.left) + [root.val] + inorder(root.right)


def is_bst(root, low=float("-inf"), high=float("inf")):
    if not root:
        return True
    if not (low < root.val < high):
        return False
    return (
        is_bst(root.left, low, root.val) and
        is_bst(root.right, root.val, high)
    )


def main():
    # --- Insert tests ---
    root = None
    for v in [5, 3, 7, 2, 4, 6, 8]:
        root = insert(root, v)

    assert inorder(root) == [2, 3, 4, 5, 6, 7, 8]
    assert is_bst(root)

    # --- Search tests ---
    assert search(root, 6) is not None
    assert search(root, 10) is None

    # --- Delete leaf ---
    root = delete(root, 2)
    assert inorder(root) == [3, 4, 5, 6, 7, 8]
    assert is_bst(root)

    # --- Delete node with one child ---
    root = delete(root, 3)
    assert inorder(root) == [4, 5, 6, 7, 8]
    assert is_bst(root)

    # --- Delete node with two children ---
    root = delete(root, 5)
    assert inorder(root) == [4, 6, 7, 8]
    assert is_bst(root)

    # --- Delete root repeatedly ---
    root = delete(root, 6)
    root = delete(root, 7)
    root = delete(root, 8)
    root = delete(root, 4)

    assert root is None  # tree should be empty

    print("All tests passed.")

main()