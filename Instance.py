# from graph_tools import Graph
from Structures import Graph


class Instance:
    def __init__(self, field):
        self.graph = self.get_graph(field)
        self.pairs, self.numbers = self.get_pairs(field)

    @staticmethod
    def is_valid(node, field):
        return 0 <= node[0] < field.height and 0 <= node[1] < field.width

    def get_graph(self, field):
        graph = Graph()

        for i in range(field.height):
            for j in range(field.width):
                node1 = i, j
                nodes = {(i + 1, j), (i, j + 1)}

                for node2 in (node for node in nodes if
                              self.is_valid(node, field)):
                    graph.add_edge(node1, node2)

        return graph

    @staticmethod
    def get_pairs(field):
        pairs = set()
        numbers = set()
        cur_pairs = dict()
        for i in range(field.height):
            for j in range(field.width):
                element = field.field[i][j]
                if element != '#':
                    numbers.add((i, j))
                    if element not in cur_pairs.keys():
                        cur_pairs[element] = (i, j)
                    else:
                        pairs.add(frozenset((cur_pairs[element], (i, j))))
        return pairs, numbers
