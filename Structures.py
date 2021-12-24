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

    def add_children(self, zero_child, one_child):
        self.zero_child = zero_child
        self.one_child = one_child

    def __eq__(self, other):
        return self.edge == other.edge and self.mate == other.mate and \
               self.arc == other.arc


class Field:
    def __init__(self, params, field):
        self.width, self.height = params
        self.field = field

TERMINAL_ZERO = Node(None, None, 0)
TERMINAL_ONE = Node(None, None, 1)
