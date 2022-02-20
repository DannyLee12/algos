"""
Given a binary tree, find its minimum depth. The minimum depth is the number
of nodes along the shortest path from the root node down to the nearest leaf
node.
"""


class Node:
    def __init__(self, node, left=None, right=None):
        self.node = node
        self.left = left
        self.right = right


def find_min_length(root: Node):
    """return the minimum length of a binary tree"""

    # Base case - end of any path
    if root.left is None and root.right is None:
        return 1

    if root.left is None:
        return find_min_length(root.right) + 1

    if root.right is None:
        return find_min_length(root.left) + 1

    return min(find_min_length(root.left), find_min_length(root.right)) + 1


if __name__ == '__main__':
    tree = Node(1, left=Node(2, Node(4), Node(5)), right=Node(3, Node(6), Node(2)))
    print(find_min_length(tree))
