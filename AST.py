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
        self.setRoot()
        current_node = self.root
        i = 0
        while i<len(self.node_values)-2:
            current_node.value = self.node_values[i]
            if len(self.node_values)-1 >= 2*i+1 :
                left = Node(self.node_values[2*i + 1])
            else:
                left = None
            if len(self.node_values)-1 >= 2*i+2:
                right = Node(self.node_values[2*i + 2])
            else:
                right = None
            current_node.left = left
            current_node.right = right
            current_node = current_node.left
            if i%2 != 0:
                i = 2*i + 1
            else:
                i += 1

    
    def pre_order_traverse(self, node):
        current_node = node
        if current_node is not None:
            print(current_node.value, end=' ')
            self.pre_order_traverse(current_node.left)
            self.pre_order_traverse(current_node.right)