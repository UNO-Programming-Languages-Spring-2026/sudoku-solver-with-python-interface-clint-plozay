import sys, clingo
from sudoku_board import Sudoku

class Context:

    def __init__(self, board: Sudoku):
        self.board = board
        
    def initial(self) -> list[clingo.symbol.Symbol]:
        atoms = []
        for k, v in self.board.sudoku.items():
            atoms.append(clingo.Tuple_([clingo.Number(k[0]), clingo.Number(k[1]), clingo.Number(v)]))
        return atoms

class ClingoApp(clingo.application.Application):
    def main(self, ctl, files):
        ctl.load(r'sudoku_py.lp')
        for f in files:
            if f[-4:] == '.txt':
                with open(f, 'r') as file:
                    sudoku = Sudoku.from_str(''.join(file.readlines()))
            else:
                ctl.load(f)
        if not files:
            ctl.load("-")
        ctl.ground(context = Context(sudoku))
        ctl.solve()

    def print_model(self, model, printer):
        s = Sudoku.from_model(model).__str__()

        print(s)
        sys.stdout.flush()

    
clingo.application.clingo_main(ClingoApp())

