# from standardizer import standardizer

# class CSE:
#     def __init__(self, control, stack, enviornment):
#         self.control=control
#         self.stack=stack
#         self.enviornment = enviornment

from Node import Node
from ControlStructureBuilder import ControlStructureBuilder

# tree = Node('gamma', [
#     Node('lambda', [
#         Node('x'),  
#         Node('+', [
#             Node('x'),
#             Node('2')
#         ])
#     ]),
#     Node('3')
# ])

# tree = Node('gamma', [
#     Node('lambda', [
#         Node('<ID:check_pos>'),
#         Node('gamma', [
#             Node('<ID:print>'),
#             Node('gamma', [
#                 Node('<ID:check_pos>'),
#                 Node('<INT:3>')
#             ])
#         ])
#     ]),
#     Node('lambda', [
#         Node('<ID:N>'),
#         Node('->', [
#             Node('ls', [
#                 Node('<ID:N>'),
#                 Node('<INT:0>')
#             ]),
#             Node("<STR:'Negative'>"),
#             Node("<STR:'Positive'>")
#         ])
#     ])
# ])

tree= Node('gamma', [
    Node('gamma', [
        Node('*'),
        Node('gamma', [
            Node('lambda', [
                Node('x'),
                Node('gamma', [
                    Node('gamma', [
                        Node('-'),
                        Node('x')
                    ]),
                    Node('1')
                ])
            ]),
            Node('4')
        ])
    ]),
    Node('2')
])


builder = ControlStructureBuilder()
control_structures = builder.build(tree)

for name, cs in control_structures.items():
    print(name, "=>", cs)
