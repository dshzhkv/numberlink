import argparse
from graph_tools import Graph
from Solver import *
from Parser import Parser


def main():
    parser = Parser()
    nl_instance = parser.parse_file()
    solver = Solver(nl_instance)
    solutions = solver.solve()
    parser.show_solutions(solutions)


if __name__ == '__main__':
    main()

