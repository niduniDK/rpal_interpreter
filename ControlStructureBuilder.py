class ControlStructureBuilder:
    def __init__(self):
        self.control_structures = {}  
        self.current_index = 0

    def build(self, node):
        self._build_control_structure(node, self.current_index, node)
        return self.control_structures
    
    def _preorder_flatten(self, node):
        result = []

        if node.value == 'tau' or node.value == 'lambda':
            result.extend(self._build_control_structure(node, self._get_new_index()))  # build control structure for tau
            # print(f"\n***Preorder flattening of tau node {node.value}: {result}")

        else: 
            result.append(node.value)  # visit root first (preorder)
        # result.append(node.value)
            # print(f"\nPreorder flattening of node {node.value}: {result}")
            if hasattr(node, 'children'):
                for child in node.children:
                    result.extend(self._preorder_flatten(child))  # recurse

        # print(f"Preorder flattening of node {node.value}: {result}")

        return result


    def _build_control_structure(self, node, index, root=None):
        # print(f"Building control structure for node: {node.value} at index: {index}")
        if f"δ{index}" not in self.control_structures:
            self.control_structures[f"δ{index}"] = []
        control_list = self.control_structures[f"δ{index}"]
       

        # Preorder: visit node first
        if node.value == 'lambda':
            new_index = self._get_new_index()
            param_node = node.children[0]
            if param_node.value == ',':
                var = [child.value for child in param_node.children]  
            else:
                var = param_node.value  
            control_list.append(('lambda', new_index, var))
            self._build_control_structure(node.children[1], new_index)


        elif node.value == 'gamma':
            control_list.append('gamma')
            for child in node.children:
                self._build_control_structure(child, index)

        elif node.value == '->':
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
            if E1.value != '->' and E1.value != 'lambda' and E1.value != 'gamma' and E1.value != 'tau':
                self.control_structures[f"δ{then_index}"] = []
                self.control_structures[f"δ{then_index}"].extend(self._preorder_flatten(E1))
            else:
                self._build_control_structure(E1, then_index)

            # For E2
            if E2.value != '->' and E2.value != 'lambda' and E2.value != 'gamma' and E2.value != 'tau':
                self.control_structures[f"δ{else_index}"] = []
                self.control_structures[f"δ{else_index}"].extend(self._preorder_flatten(E2))
            else:
                self._build_control_structure(E2, else_index)

                
        elif node.value == 'tau':
            # print("This is the tau node:", [node.value for node in node.children])
            control_list.append(('𝜏', len(node.children)))
            # print("new control_list:", control_list, '\n')
            for child in node.children:
                self._build_control_structure(child, index)

        elif node.value in ['+', '-', '**', '*', '/', 'eq', 'le','not','ls','neg','gr','ge','ne']:
            #control_list.append(node.value)
            control_list.extend(self._preorder_flatten(node))

        elif node.value == 'aug':
            control_list.extend(self._preorder_flatten(node))

        else:
            # Literal or identifier
            control_list.append(node.value)
        
        return control_list
            

    def _get_new_index(self):
        self.current_index += 1
        return self.current_index
