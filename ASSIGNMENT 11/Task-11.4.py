class BSTNode:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

class BST:
    def __init__(self):
        self.root = None

    def insert(self, key):
        self.root = self._insert_recursive(self.root, key)

    def _insert_recursive(self, node, key):
        if node is None:
            return BSTNode(key)
        if key < node.key:
            node.left = self._insert_recursive(node.left, key)
        elif key > node.key:
            node.right = self._insert_recursive(node.right, key)
        # Duplicate keys are not inserted in BST
        return node

    def inorder_traversal(self):
        result = []
        self._inorder_helper(self.root, result)
        return result

    def _inorder_helper(self, node, result):
        if node:
            self._inorder_helper(node.left, result)
            result.append(node.key)
            self._inorder_helper(node.right, result)
# Test
if __name__ == "__main__":
    bst = BST()
    for key in [50, 30, 70, 20, 60]:
        bst.insert(key)
    print("Binary Search Tree Demonstration")
    print("Keys inserted:", [50, 30, 70, 20, 60])
    print("Inorder Traversal:", bst.inorder_traversal())


