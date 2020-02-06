class Node:
    def __init__(self, value):
        self.right = None
        self.left = None
        self.value = value


def insert(root, node):
    if root is None:
        root = node
    else:
        if root.value < node.value:
            if root.right is None:
                root.right = node
            else:
                insert(root.right, node)
        elif root.value > node.value:
            if root.left is None:
                root.left = node
            else:
                insert(root.left, node)
        else:
            print("The value is alread present in the Binary search tree")

# def printInorder(root):
#     if root.left is None