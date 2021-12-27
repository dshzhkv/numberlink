import itertools

from Application.Structures import *


class Solver:
    def __init__(self, instance):
        self.instance = instance

    def solve(self):
        edges = self.instance.graph.edges
        vertices = {'active': self.instance.graph.vertices, 'not_active': []}

        root = Node(edges[0], {v: v for v in vertices['active']}, 1)
        nodes = [root]

        for i in range(len(edges)):
            edge = edges.pop(0)
            next_edge = edges[0] if edges else None
            self.update_vertices(edge, vertices, edges)

            new_nodes = []

            for node in nodes:
                node.add_zero_child(self.get_zero_child(node, vertices,
                                                        next_edge))
                node.add_one_child(self.get_one_child(node, vertices,
                                                      next_edge))
                self.get_new_nodes(node.zero_child, node.one_child, new_nodes)

            nodes = new_nodes

        return self.collect_solutions(root)

    def get_zero_child(self, node, vertices, next_edge):
        if self.is_zero_incompatible(node, self.instance, vertices):
            return TERMINAL_ZERO
        else:
            new_mate = self.update_domain(node.mate, vertices)
            return self.get_node(next_edge, new_mate, 0)

    def get_one_child(self, node, vertices, next_edge):
        if self.is_one_incompatible(node, self.instance, vertices):
            return TERMINAL_ZERO
        else:
            new_mate = self.update_domain(self.update_mate(node),
                                          vertices)
            return self.get_node(next_edge, new_mate, 1)

    def get_new_nodes(self, zero_child, one_child, new_nodes):
        if not self.is_terminal(zero_child):
            new_nodes.append(zero_child)
        if not self.is_terminal(one_child):
            new_nodes.append(one_child)

    @staticmethod
    def is_terminal(node):
        return node == TERMINAL_ONE or node == TERMINAL_ZERO

    @staticmethod
    def update_vertices(edge, vertices, edges):
        incident_vertices = set(itertools.chain(*edges))
        edge_incident_vertices = [v for v in edge if v not in
                                  incident_vertices]
        for v in edge_incident_vertices:
            vertices['active'].remove(v)
            vertices['not_active'].append(v)

    @staticmethod
    def is_zero_incompatible(node, instance, vertices):
        filtered = [v for v in node.edge if v not in vertices['active']]
        for v in filtered:
            if node.mate[v] == v or v not in instance.numbers and \
                    node.mate[v] not in [0, v]:
                return True
        return False

    @staticmethod
    def update_domain(mate, vertices):
        return {v: mate[v] for v in vertices['active']}

    def update_mate(self, node):
        mate = {}

        for vertex in node.mate:
            if vertex in node.edge and node.mate[vertex] != vertex:
                mate[vertex] = 0
            elif node.mate[vertex] in node.edge:
                opposite = self.get_opposite(node.mate[vertex], node.edge)
                mate[vertex] = node.mate[opposite]
            else:
                mate[vertex] = node.mate[vertex]

        return mate

    @staticmethod
    def get_node(next_edge, new_mate, arc):
        return Node(next_edge, new_mate, arc) if next_edge else TERMINAL_ONE

    def is_one_incompatible(self, node, instance, vertices):
        union = instance.numbers | set(vertices['not_active'])
        pairs = {node.mate[v] for v in node.edge}

        def condition(v):
            return (v in instance.numbers and node.mate[v] != v
                    or node.mate[v] in [0, self.get_opposite(v, node.edge)])

        return (pairs <= union and pairs not in instance.pairs
                or any(condition(v) for v in node.edge))

    @staticmethod
    def get_opposite(vertice, edge):
        return edge[0] if vertice == edge[1] else edge[1] \
            if vertice == edge[0] else None

    def collect_solutions(self, root, path=None):
        if path is None:
            path = []
        if root is TERMINAL_ONE:
            yield path
        elif root is not TERMINAL_ZERO:
            yield from itertools.chain(
                self.collect_solutions(root.zero_child, path),
                self.collect_solutions(root.one_child, path + [root.edge]))