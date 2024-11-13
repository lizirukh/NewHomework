# printLeafNodes, countEdges

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def printLeafNodes(root):
    if root is None:
        return

    if root.left is None and root.right is None:
        print(root.data, end=" ")

    if root.left is not None:
        printLeafNodes(root.left)
    if root.right is not None:
        printLeafNodes(root.right)

def countEdges(root):
    def countNodes(node):
        if node is None:
            return 0
        return 1 + countNodes(node.left) + countNodes(node.right)

    total_nodes = countNodes(root)
    
    return max(0, total_nodes - 1)

                                             # 4
                                           #  / \
                                        #    9   11
                                        #   / \  / \
                                       #   1  6  7  3

root = Node(4)
root.left = Node(9)
root.right = Node(11)
root.left.left = Node(1)
root.left.right = Node(6)
root.right.left = Node(7)
root.right.right = Node(3)

print('Leaf nodes of the binary tree are:')
printLeafNodes(root)

print(f'\nNumber of edges in the binary tree: {countEdges(root)}')
