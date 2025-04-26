class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


class AST:
    def __init__(self, node_values=None):
        self.root = None
        self.node_values = node_values if node_values is not None else []


    def setRoot(self):
        self.root = Node(self.node_values[0])

    
    def build_AST(self):
        if not self.node_values:
            return []