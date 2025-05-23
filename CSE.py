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

tree = Node('gamma', [
    Node('lambda', [
        Node('<ID:check_pos>'),
        Node('gamma', [
            Node('<ID:print>'),
            Node('gamma', [
                Node('<ID:check_pos>'),
                Node('<INT:3>')
            ])
        ])
    ]),
    Node('lambda', [
        Node('<ID:N>'),
        Node('->', [
            Node('ls', [
                Node('<ID:N>'),
                Node('<INT:0>')
            ]),
            Node("<STR:'Negative'>"),
            Node("<STR:'Positive'>")
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