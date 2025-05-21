class Node:
    def __init__(self, label, children=None):
        self.label = label
        self.children = children or []
