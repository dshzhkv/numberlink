import argparse
from graph_tools import Graph

from CUI import CUI
from Solver import *
from Parser import Parser


def main():
    cui = CUI()
    instance = cui.get_instance()
    solver = Solver(instance)
    solutions = solver.solve()
    cui.show_solutions(solutions)


if __name__ == '__main__':
    main()

