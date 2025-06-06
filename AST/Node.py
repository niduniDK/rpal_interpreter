class Node:
    def __init__(self, value, children=None):
        self.value = value
        self.children = children or []
