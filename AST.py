class Node:
    def __init__(self, value, children=None):
        self.value = value
        self.children = children if children is not None else []

class AST:
    def __init__(self, root):
        self.root = root
        # self.node_values = node_values if node_values is not None else []
    
    def pre_order_traverse(self, node, dots=0, visited=None):
        if visited is None:
            visited = set()
        if id(node) in visited:
            return
        visited.add(id(node))
        if node: 
            print(dots*'.'+str(node.value))
            for child in node.children:
                self.pre_order_traverse(node=child, visited=visited, dots=dots+1)
        else: 
            print(" ")
        