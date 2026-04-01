import sys, clingo
from sudoku_board import Sudoku
class ClingoApp(clingo.application.Application):
    def main(self, ctl, files):
        ctl.load(r'sudoku2.lp')
        for f in files:
            ctl.load(f)
        if not files:
            ctl.load("-")
        ctl.ground()
        ctl.solve()

    def print_model(self, model, printer):
        s = Sudoku.from_model(model).__str__()

        print(s)
        sys.stdout.flush()

    
clingo.application.clingo_main(ClingoApp())