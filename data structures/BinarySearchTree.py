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
            pass


def printInorder(root):
    if root:
        printInorder(root.left)
        print(root.value)
        printInorder(root.right)





a = [8, 3, 10, 1, 6, 14, 13, 7, 4]
root_val = Node(a[0])
for x in a:
    insert(root_val, Node(x))

printInorder(root_val)


def same_height_nodes(root):
    list_of_nodes, k, list_of_nodes_temp = [root], 1, []
    if root:
        print("Height wise printing starts: ")
        print()
    print(root.value)
    while k == 1:
        k = 0
        for node in list_of_nodes:
            if node.left:
                print(node.left.value, end=" ")
                list_of_nodes_temp.append(node.left)
                k = 1
            if node.right:
                print(node.right.value, end=" ")
                list_of_nodes_temp.append(node.right)
                k = 1
        print()
        list_of_nodes = list_of_nodes_temp.copy()
        list_of_nodes_temp.clear()


same_height_nodes(root_val)
