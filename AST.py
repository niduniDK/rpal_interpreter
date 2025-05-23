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
        # if id(node) in visited:
        #     return
        visited.add(id(node))
        if node: 
            print(dots*'.'+str(node.value))
            for child in node.children:
                self.pre_order_traverse(node=child, visited=visited, dots=dots+1)
        else: 
            print(" ")

    #Added by Raleesa    
    def parse_dot_tree(self, dot_lines):
        stack = []
        root = None

        for line in dot_lines:
            stripped = line.lstrip('.')
            value = eval(stripped) if stripped.isdigit() or stripped.startswith("'") else stripped
            level = len(line) - len(stripped)

            node = {'value': value, 'children': []}

            while len(stack) > level:
                stack.pop()

            if stack:
                stack[-1]['children'].append(node)
            else:
                root = node

            stack.append(node)

        def build_node(d):
            return Node(d['value'], [build_node(c) for c in d['children']])

        return build_node(root)   
    
    def to_code(self,node, indent=0):
        ind = '    ' * indent
        if not node.children:
            return f"{ind}Node({repr(node.value)})"
        children_code = ',\n'.join(self.to_code(child, indent + 1) for child in node.children)
        return f"{ind}Node({repr(node.value)}, [\n{children_code}\n{ind}])" 
    
    def get_dot_lines(self, node, dots=0, lines=None):
        if lines is None:
            lines = []
        if node:
            lines.append(dots * '.' + str(node.value))
            for child in node.children:
                self.get_dot_lines(child, dots + 1, lines)
        return lines