# from standardizer import standardizer

# class CSE:
#     def __init__(self, control, stack, enviornment):
#         self.control=control
#         self.stack=stack
#         self.enviornment = enviornment

from Node import Node
from ControlStructureBuilder import ControlStructureBuilder
from CSE_machine import CSEMachine

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
                    Node(1)
                ])
            ]),
            Node(4)
        ])
    ]),
    Node(2)
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