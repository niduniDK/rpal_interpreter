from AST.parser import parser
from AST.AST import Node, AST

def standardizer(node):
    if node.value == 'let':
        temp_children = node.children
        new_children = []
        node.children = []
        node.value = 'gamma'
        if temp_children[0]:
            temp = Node('lambda', [temp_children[0].children[0], temp_children[1]])
            new_children.append(temp)
            new_children.append(temp_children[0].children[1])
        
        node.children = new_children
    
    elif node.value == 'where':
        temp_children = node.children
        new_children = []
        node.children = []
        node.value = 'gamma'
        if temp_children[1]:
            temp = Node('lambda', [temp_children[1].children[0], temp_children[0]])
            new_children.append(temp)
            new_children.append(temp_children[1].children[1])
        node.children = new_children

    elif node.value == 'within':
        temp_children = node.children
        new_children = []
        node.children = []
        node.value = '='
        if temp_children[1] and temp_children[0]:
            left_child = temp_children[1].children[0]
            temp = Node('lambda', [temp_children[0].children[0], temp_children[1].children[1]])
            right_child = Node('gamma', [temp, temp_children[0].children[1]])
            new_children.append(left_child)
            new_children.append(right_child)
        
        node.children = new_children

    elif node.value == 'function_form':
        temp_children = node.children
        new_children = []
        node.children = []
        node.value = '='

        repeating_struct = Node('lambda')
        curr = repeating_struct

        for i in range(1, len(temp_children) - 1):
            curr.children.append(temp_children[i])
            if i != len(temp_children) - 2:
                curr.children.append(Node('lambda'))
            else:
                curr.children.append(temp_children[-1])
            curr = curr.children[1]
        
        new_children.append(temp_children[0])
        new_children.append(repeating_struct)
        node.children = new_children

    elif node.value == '@':
        temp_children = node.children
        new_children = []
        node.children = []
        node.value = 'gamma'

        if temp_children:
            temp = Node('gamma', [temp_children[1], temp_children[0]])
            new_children.append(temp)
            new_children.append(temp_children[2])
        node.children = new_children
    
    elif node.value == 'rec':
        temp_children = node.children
        new_children = []
        node.children = []
        node.value = '='

        if temp_children[0]:
            temp1 = Node('lambda', [temp_children[0].children[0], temp_children[0].children[1]])
            temp2 = Node('<Y*>')
            temp3 = Node('gamma', [temp2, temp1])
            new_children.append(temp_children[0].children[0])
            new_children.append(temp3)

        node.children = new_children

    elif node.value == 'lambda':
        temp_children = node.children
        new_children = []
        node.children = []
        repeating_struct = Node('lambda')
        curr = repeating_struct

        for i in range(1, len(temp_children)-1):
            curr.children.append(temp_children[i])
            if i != len(temp_children) - 2:
                temp = Node('lambda')
                curr.children.append(temp)
                curr = temp
            else:
                curr.children.append(temp_children[-1])
        
        new_children.append(temp_children[0])
        if len(temp_children) > 2: new_children.append(repeating_struct)
        else: new_children.append(temp_children[1])

        node.children = new_children

    elif node.value == 'and':
        temp_children = node.children
        new_children = []
        node.children = []
        node.value = '='

        if temp_children:
            left = Node(',')
            right = Node('tau')
            
            for child in temp_children:
                left.children.append(child.children[0])
                right.children.append(child.children[1])
            new_children.append(left)
            new_children.append(right)
        
        node.children = new_children
    
    return node

def get_standardized_tree(node):
    for i, child in enumerate(node.children):
        if child:
            node.children[i] = get_standardized_tree(child)
    return standardizer(node)


def standardize_ast(source_code):
    root = parser(source_code)
    ast = AST(root)
    std_root = get_standardized_tree(root)
    
    tree_new = ast.get_dot_lines(std_root)
    tree = ast.parse_dot_tree(tree_new)

    return tree  # return ast and tree so return_tree can use them

def print_st(source_code):
    root = parser(source_code)
    ast = AST(root)
    std_root = get_standardized_tree(root)
    ast.pre_order_traverse(std_root)