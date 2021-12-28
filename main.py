from UI.CUI import CUI
from Application.Solver import *


def main():
    cui = CUI()
    instance = cui.get_instance()
    solver = Solver(instance)
    solutions = solver.solve()
    cui.show_solutions(solutions)


if __name__ == '__main__':
    main()

