class Node:
    def __init__(self, edge, mate, arc):
        self.edge = edge
        self.mate = mate
        self.arc = arc
        self.zero_child = None
        self.one_child = None

    def add_zero_child(self, child):
        self.zero_child = child

    def add_one_child(self, child):
        self.one_child = child


class Field:
    def __init__(self, params, field):
        self.width, self.height = params
        self.field = field


class Graph:
    def __init__(self):
        self.edges = []
        self.vertices = set()

    def add_edge(self, v1, v2):
        self.vertices.add(v1)
        self.vertices.add(v2)
        self.edges.append([v1, v2])


TERMINAL_ZERO = Node(None, None, 0)
TERMINAL_ONE = Node(None, None, 1)
