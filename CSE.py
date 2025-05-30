from Node import Node
from ControlStructureBuilder import ControlStructureBuilder
from CSE_machine import CSEMachine

# tree= Node('gamma', [
#     Node('gamma', [
#         Node('*'),
#         Node('gamma', [
#             Node('lambda', [
#                 Node('x'),
#                 Node('gamma', [
#                     Node('gamma', [
#                         Node('-'),
#                         Node('x')
#                     ]), 
#                     Node(1)
#                 ])
#             ]),
#             Node(4)
#         ])
#     ]),
#     Node(2)
# ])


# tree = Node('gamma', [
#     Node('lambda', [
#         Node('<ID:f>'),
#         Node('gamma', [
#             Node('lambda', [
#                 Node('<ID:fib>'),
#                 Node('gamma', [
#                     Node('<ID:Print>'),
#                     Node('gamma', [
#                         Node('<ID:fib>'),
#                         Node('<INT:5>')
#                     ])
#                 ])
#             ]),
#             Node('gamma', [
#                 Node('<Y*>'),
#                 Node('lambda', [
#                     Node('<ID:fib>'),
#                     Node('lambda', [
#                         Node('<ID:n>'),
#                         Node('->', [
#                             Node('eq', [
#                                 Node('<ID:n>'),
#                                 Node('<INT:0>')
#                             ]),
#                             Node('<nil>'),
#                             Node('aug', [
#                                 Node('gamma', [
#                                     Node('<ID:fib>'),
#                                     Node('-', [
#                                         Node('<ID:n>'),
#                                         Node('<INT:1>')
#                                     ])
#                                 ]),
#                                 Node('gamma', [
#                                     Node('<ID:f>'),
#                                     Node('<ID:n>')
#                                 ])
#                             ])
#                         ])
#                     ])
#                 ])
#             ])
#         ])
#     ]),
#     Node('gamma', [
#         Node('<Y*>'),
#         Node('lambda', [
#             Node('<ID:f>'),
#             Node('lambda', [
#                 Node('<ID:n>'),
#                 Node('->', [
#                     Node('eq', [
#                         Node('<ID:n>'),
#                         Node('<INT:1>')
#                     ]),
#                     Node('<INT:0>'),
#                     Node('->', [
#                         Node('eq', [
#                             Node('<ID:n>'),
#                             Node('<INT:2>')
#                         ]),
#                         Node('<INT:1>'),
#                         Node('+', [
#                             Node('gamma', [
#                                 Node('<ID:f>'),
#                                 Node('-', [
#                                     Node('<ID:n>'),
#                                     Node('<INT:1>')
#                                 ])
#                             ]),
#                             Node('gamma', [
#                                 Node('<ID:f>'),
#                                 Node('-', [
#                                     Node('<ID:n>'),
#                                     Node('<INT:2>')
#                                 ])
#                             ])
#                         ])
#                     ])
#                 ])
#             ])
#         ])
#     ])
# ])

tree = Node('gamma', [
    Node('lambda', [
        Node('<ID:check_pos>'),
        Node('gamma', [
            Node('<ID:print>'),
            Node('gamma', [
                Node('<ID:check_pos>'),
                Node('<INT:5>')
            ])
        ])
    ]),
    Node('lambda', [
        Node('<ID:N>'),
        Node('->', [
            Node('eq', [
                Node('<ID:N>'),
                Node('<INT:0>')
            ]),
            Node("<STR:'Positive'>"),
            Node("<STR:'Negative'>")
        ])
    ])
])


builder = ControlStructureBuilder()
control_structures = builder.build(tree)

print('\nControl Structures for the CSE Machine :\n')
for name, cs in control_structures.items():
    print(name, "=>", cs)

machine = CSEMachine(control_structures)
print('\n===================================================================')
result = machine.run()
print('=====================================================================')
print("Final Result:", result)