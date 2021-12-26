from Structures import Graph
import math


class Instance:
    def __init__(self, field, is_hexagonal):
        self.is_hexagonal = is_hexagonal
        self.graph = self.get_graph(field)
        self.pairs, self.numbers = self.get_pairs(field)

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

        if self.is_hexagonal:
            return self.get_incident_nodes_hexagonal(i, j, passed_middle,
                                                     width, height)

        return self.get_incident_nodes_rectangle(i, j, width, height)

    @staticmethod
    def get_incident_nodes_hexagonal(i, j, passed_middle, width, height):
        down = (i + 1, j)
        right = (i, j + 1)
        diagonal_right = (i + 1, j + 1)
        diagonal_left = (i + 1, j - 1)

        nodes = set()

        if not passed_middle:
            nodes.add(down)
            if j < width - 1:
                nodes.add(right)
            nodes.add(diagonal_right)
        else:
            if j < width - 1:
                if i < height - 1:
                    nodes.add(down)
                nodes.add(right)
            if j > 0 and i < height - 1:
                nodes.add(diagonal_left)

        return nodes

    def get_incident_nodes_rectangle(self, i, j, width, height):
        nodes = {(i + 1, j), (i, j + 1)}
        return {n for n in nodes if self.is_valid(n, width, height)}

    @staticmethod
    def is_valid(node, width, height):
        return 0 <= node[0] < height and 0 <= node[1] < width

    @staticmethod
    def add_edges(node1, nodes, graph):
        for node2 in nodes:
            graph.add_edge(node1, node2)

    def get_pairs(self, field):
        pairs = set()
        numbers = set()
        cur_pairs = dict()
        paired = set()
        for i in range(field.height):
            for j in range(len(field.field[i])):
                element = field.field[i][j]
                if element != '#':
                    self.check_for_excess_numbers(element, paired)
                    numbers.add((i, j))
                    if element not in cur_pairs.keys():
                        cur_pairs[element] = (i, j)
                    else:
                        pairs.add(frozenset((cur_pairs[element], (i, j))))
                        paired.add(element)
                        del cur_pairs[element]

        self.check_for_no_pair(cur_pairs)

        return pairs, numbers

    @staticmethod
    def check_for_no_pair(cur_pairs):
        if len(cur_pairs) > 0:
            raise ValueError('У некоторых чисел нет пары :(')

    @staticmethod
    def check_for_excess_numbers(element, paired):
        if element in paired:
            raise ValueError('На поле не может быть больше двух одинаковых '
                             'чисел')
