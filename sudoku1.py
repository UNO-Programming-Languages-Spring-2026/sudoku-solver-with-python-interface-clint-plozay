import sys, clingo
class ClingoApp(clingo.application.Application):
    def main(self, ctl, files):
        for f in files:
            ctl.load(f)
        if not files:
            ctl.load("-")
        ctl.ground()
        ctl.solve()
clingo.application.clingo_main(ClingoApp())