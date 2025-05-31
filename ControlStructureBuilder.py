class ControlStructureBuilder:
    def __init__(self):
        self.control_structures = {}  
        self.current_index = 0

    def build(self, node):
        self._build_control_structure(node, self.current_index, node)
        return self.control_structures
    
    def _preorder_flatten(self, node):
        result = []

        result.append(node.label)  # visit root first (preorder)

        if hasattr(node, 'children'):
            for child in node.children:
                result.extend(self._preorder_flatten(child))  # recurse

        return result


    def _build_control_structure(self, node, index, root=None):
        if f"δ{index}" not in self.control_structures:
            self.control_structures[f"δ{index}"] = []
        control_list = self.control_structures[f"δ{index}"]
       

        # Preorder: visit node first
        if node.label == 'lambda':
            new_index = self._get_new_index()
            param_node = node.children[0]
            if param_node.label == ',':
                var = [child.label for child in param_node.children]  
            else:
                var = param_node.label  
            control_list.append(('lambda', new_index, var))
            self._build_control_structure(node.children[1], new_index)


        elif node.label == 'gamma':
            control_list.append('gamma')
            for child in node.children:
                self._build_control_structure(child, index)

        elif node.label == '->':
            B = node.children[0]
            E1 = node.children[1]
            E2 = node.children[2]

            # Step 1: Generate new δ indices for E1 and E2
            then_index = self._get_new_index()
            else_index = self._get_new_index()

            # Step 2: Append δ_then, δ_else, and 'b'
            control_list.append(f"δ{then_index}")
            control_list.append(f"δ{else_index}")
            control_list.append("β")

            # Step 3: Append preorder traversal of B
            b_preorder = self._preorder_flatten(B)
            control_list.extend(b_preorder)

            # Step 4: Build control structures for E1 and E2 in their respective δs
            #self._build_control_structure(E1, then_index)
            #self._build_control_structure(E2, else_index)

            # Add full preorder of E1 to δ{then_index}
            #self.control_structures[f"δ{then_index}"] = []
            #self.control_structures[f"δ{then_index}"].extend(self._preorder_flatten(E1))

            # Add full preorder of E2 to δ{else_index}
            #self.control_structures[f"δ{else_index}"] = []
            #self.control_structures[f"δ{else_index}"].extend(self._preorder_flatten(E2))

            # For E1
            if E1.label != '->':
                self.control_structures[f"δ{then_index}"] = []
                self.control_structures[f"δ{then_index}"].extend(self._preorder_flatten(E1))
            else:
                self._build_control_structure(E1, then_index)

            # For E2
            if E2.label != '->':
                self.control_structures[f"δ{else_index}"] = []
                self.control_structures[f"δ{else_index}"].extend(self._preorder_flatten(E2))
            else:
                self._build_control_structure(E2, else_index)



                
        elif node.label == 'tau':
            control_list.append(('𝜏', len(node.children)))
            for child in node.children:
                self._build_control_structure(child, index)

        elif node.label in ['+', '-', '*', '/', 'eq', 'le','not','ls','neg','gr','ge','ne']:
            #control_list.append(node.label)
            control_list.extend(self._preorder_flatten(node))

        else:
            # Literal or identifier
            control_list.append(node.label)

    def _get_new_index(self):
        self.current_index += 1
        return self.current_index
