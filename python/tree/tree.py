"""Basic tree structure allowing multiple childern per node"""

from typing import Any, List, Optional
from collections import deque

class TreeNode:
    parent: Optional['TreeNode']
    children: Optional[List['TreeNode']]

    def __init__(self, parent: 'TreeNode', value: Any):
        self.parent = parent
        self.children = []
        self.value = value

class Tree:

    root: Optional[TreeNode]

    def __init__(self, root_value: Any):

        self.root = TreeNode(None, root_value)

    @staticmethod
    def add_node(parent: TreeNode, value: Any):
        new_node = TreeNode(parent, value)
        parent.children.append(new_node)
        return new_node

    def depth_first_traversal(self, node: Optional[TreeNode] = None):
        if node is None:
            node = self.root

        if len(node.children) != 0:
            for child in node.children:
                self.depth_first_traversal(child)

        print(node.value, end=" ")

    def breadth_first_traversal(self, node: Optional[TreeNode] = None):

        if node is None:
            node = self.root

        nodes_to_visit = deque([node])
        while len(nodes_to_visit) != 0:
            current_node = nodes_to_visit.popleft()
            print(current_node.value, end=" ")
            nodes_to_visit.extend(current_node.children)
