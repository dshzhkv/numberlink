from Structures import Graph
import math

class Instance:
    def __init__(self, field, is_hexagonal):
        self.is_hexagonal = is_hexagonal
        self.graph = self.get_graph(field)
        self.pairs, self.numbers = self.get_pairs(field)

    def is_valid(self, node, width, height):
        return 0 <= node[0] < height and 0 <= node[1] < width

    def get_graph(self, field):
        graph = Graph()

        passed_middle = False

        for i in range(field.height):
            width = len(field.field[i])

            if not passed_middle:
                passed_middle = (width == field.width)

            for j in range(width):
                nodes = self.get_incident_nodes(i, j, width, field.height,
                                                passed_middle)
                self.add_edges((i, j), nodes, graph)

        return graph

    def get_incident_nodes(self, i, j, width, height, passed_middle):
        nodes = set()
        if self.is_hexagonal:
            if not passed_middle:
                nodes.add((i + 1, j))
                if j < width - 1:
                    nodes.add((i, j + 1))
                nodes.add((i + 1, j + 1))
            else:
                if i == height - 1:
                    if j < width - 1:
                        nodes.add((i, j + 1))
                else:
                    if j < width - 1:
                        nodes.add((i + 1, j))
                        nodes.add((i, j + 1))
                    if j > 0:
                        nodes.add((i + 1, j - 1))
        else:
            nodes = {(i + 1, j), (i, j + 1)}
            nodes = {node for node in nodes if self.is_valid(node, width, height)}

        return nodes

    @staticmethod
    def get_diagonal_nodes(i, j, passed_middle, height, nodes):
        if passed_middle:
            if j > 0 and i + 1 < height:
                nodes.add((i + 1, j - 1))
        else:
            nodes.add((i + 1, j + 1))

    @staticmethod
    def add_edges(node1, nodes, graph):
        for node2 in nodes:
            graph.add_edge(node1, node2)

    @staticmethod
    def get_pairs(field):
        pairs = set()
        numbers = set()
        cur_pairs = dict()
        for i in range(field.height):
            for j in range(len(field.field[i])):
                element = field.field[i][j]
                if element != '#':
                    numbers.add((i, j))
                    if element not in cur_pairs.keys():
                        cur_pairs[element] = (i, j)
                    else:
                        pairs.add(frozenset((cur_pairs[element], (i, j))))
        return pairs, numbers
