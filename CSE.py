from Node import Node
from ControlStructureBuilder import ControlStructureBuilder
from CSE_machine import CSEMachine
from standardizer import standardize_ast


def evaluate(source_code):
    tree = standardize_ast(source_code)
    builder = ControlStructureBuilder()
    control_structures = builder.build(tree)

    # print('\nControl Structures for the CSE Machine :\n')
    # for name, cs in control_structures.items():
    #     print(name, "=>", cs)

    machine = CSEMachine(control_structures)
    result = machine.run()
    # print("Final Result:", result)
    return result
