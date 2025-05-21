class ControlStructureBuilder:
    def __init__(self):
        self.control_structures = {}  # δ0, δ1, ...
        self.current_index = 0

    def build(self, node):
        self._build_control_structure(node, self.current_index, node)
        return self.control_structures

    def _build_control_structure(self, node, index, root=None):
        if f"δ{index}" not in self.control_structures:
            self.control_structures[f"δ{index}"] = []
        control_list = self.control_structures[f"δ{index}"]

        # Preorder: visit node first
        if node.label == 'lambda':
            new_index = self._get_new_index()
            var = node.children[0].label
            control_list.append(('lambda', new_index, var))

            # Recursively build lambda body in δk
            self._build_control_structure(node.children[1], new_index)

        elif node.label == 'gamma':
            control_list.append('gamma')
            for child in node.children:
                self._build_control_structure(child, index)

        elif node.label == 'tau':
            control_list.append(('tau', len(node.children)))
            for child in node.children:
                self._build_control_structure(child, index)

        elif node.label in ['+', '-', '*', '/', 'eq', 'lt', 'not']:
            control_list.append(node.label)

        else:
            # Literal or identifier
            control_list.append(node.label)

    def _get_new_index(self):
        self.current_index += 1
        return self.current_index
